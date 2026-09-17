import os
import json
import re

import faiss
import numpy as np

from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from huggingface_hub import InferenceClient


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError(
        "HF_TOKEN not found in .env file."
    )


# ============================================================
# HUGGING FACE LLM
# ============================================================

MODEL_NAME = "deepseek-ai/DeepSeek-V3-0324"

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="auto"
)


# ============================================================
# PDF TEXT EXTRACTION
# ============================================================

def extract_text_from_pdf(pdf_path):

    reader = PdfReader(pdf_path)

    all_text = ""

    for page in reader.pages:

        text = page.extract_text()

        if text:
            all_text += text + "\n"

    return all_text


# ============================================================
# CHUNKING
# ============================================================

def create_chunks(text):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100
    )

    chunks = text_splitter.split_text(text)

    return chunks


# ============================================================
# VECTOR DATABASE
# ============================================================

def create_vector_database(chunks):

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    embeddings = embedding_model.embed_documents(
        chunks
    )

    vectors = np.array(
        embeddings
    ).astype("float32")

    dimension = vectors.shape[1]

    vector_db = faiss.IndexFlatL2(
        dimension
    )

    vector_db.add(vectors)

    return embedding_model, vector_db


# ============================================================
# RETRIEVAL
# ============================================================

def retrieve_chunks(
    question,
    embedding_model,
    vector_db,
    chunks,
    k=3
):

    question_embedding = (
        embedding_model.embed_query(question)
    )

    query_vector = np.array(
        [question_embedding]
    ).astype("float32")

    k = min(k, len(chunks))

    distances, indices = vector_db.search(
        query_vector,
        k
    )

    relevant_chunks = []

    for index in indices[0]:

        if index != -1:
            relevant_chunks.append(
                chunks[index]
            )

    return relevant_chunks


# ============================================================
# LLM GENERATION
# ============================================================

def generate_llm_response(
    prompt,
    max_tokens=500
):

    response = client.chat.completions.create(

        model=MODEL_NAME,

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        max_tokens=max_tokens,

        temperature=0.2
    )

    return response.choices[0].message.content


# ============================================================
# RAG ANSWER
# ============================================================

def generate_answer(
    question,
    relevant_chunks
):

    context = "\n\n".join(
        relevant_chunks
    )

    prompt = f"""
You are an AI study assistant.

Answer the student's question using ONLY
the provided study material.

Do not use outside knowledge.

If the answer is not present in the
provided study material, say:

"I couldn't find this information
in the provided document."

Keep the answer simple and accurate.

STUDY MATERIAL:

{context}

QUESTION:

{question}
"""

    try:

        return generate_llm_response(
            prompt,
            max_tokens=400
        )

    except Exception as e:

        print(
            "Hugging Face answer error:",
            e
        )

        return (
            "The AI generation service is "
            "temporarily unavailable."
        )


# ============================================================
# CLEAN JSON
# ============================================================

def clean_json_response(response_text):

    if not response_text:
        return ""

    text = response_text.strip()

    text = re.sub(
        r"^```json\s*",
        "",
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r"^```\s*",
        "",
        text
    )

    text = re.sub(
        r"\s*```$",
        "",
        text
    )

    text = text.strip()

    start = text.find("[")

    end = text.rfind("]")

    if start != -1 and end != -1:

        text = text[
            start:end + 1
        ]

    return text.strip()


# ============================================================
# MCQ GENERATION
# ============================================================

def generate_mcqs(
    relevant_chunks,
    number_of_questions=5
):

    context = "\n\n".join(
        relevant_chunks
    )

    prompt = f"""
You are an AI study assistant.

Create exactly {number_of_questions}
multiple-choice questions using ONLY
the provided study material.

IMPORTANT RULES:

1. Return ONLY a JSON array.
2. Do NOT use markdown.
3. Do NOT write anything before or after JSON.
4. Every question must have four options.
5. Options must be A, B, C, and D.
6. The answer must be A, B, C, or D.
7. Give a short explanation.
8. Use only the provided study material.

Use exactly this format:

[
  {{
    "question": "Question text",
    "options": {{
      "A": "Option A",
      "B": "Option B",
      "C": "Option C",
      "D": "Option D"
    }},
    "answer": "A",
    "explanation": "Short explanation"
  }}
]

STUDY MATERIAL:

{context}
"""

    try:

        response = generate_llm_response(
            prompt,
            max_tokens=1200
        )

        print("\nHugging Face MCQ response:")
        print(response)

        cleaned_response = (
            clean_json_response(response)
        )

        mcqs = json.loads(
            cleaned_response
        )

        if not isinstance(
            mcqs,
            list
        ):
            return "[]"

        valid_mcqs = []

        for mcq in mcqs:

            if not isinstance(
                mcq,
                dict
            ):
                continue

            if "question" not in mcq:
                continue

            if "options" not in mcq:
                continue

            if "answer" not in mcq:
                continue

            if "explanation" not in mcq:
                continue

            options = mcq["options"]

            if not isinstance(
                options,
                dict
            ):
                continue

            required_options = [
                "A",
                "B",
                "C",
                "D"
            ]

            if not all(
                option in options
                for option in required_options
            ):
                continue

            if mcq["answer"] not in required_options:
                continue

            valid_mcqs.append(
                mcq
            )

        valid_mcqs = valid_mcqs[
            :number_of_questions
        ]

        return json.dumps(
            valid_mcqs,
            ensure_ascii=False
        )

    except Exception as e:

        print(
            "Hugging Face MCQ error:",
            e
        )

        return "[]"


# ============================================================
# WEAK TOPIC ANALYSIS
# ============================================================

def analyze_weak_topics(
    wrong_questions
):

    if not wrong_questions:

        return (
            "Excellent! You answered "
            "all questions correctly."
        )

    wrong_text = ""

    for mcq in wrong_questions:

        correct_answer = mcq["answer"]

        wrong_text += f"""

Question:
{mcq["question"]}

Correct Answer:
{correct_answer}. {mcq["options"][correct_answer]}

Explanation:
{mcq["explanation"]}

"""

    prompt = f"""
You are an AI study assistant.

Analyze the student's incorrect quiz
questions.

Identify the concepts that need revision.

Give:

1. Weak Topic
2. Why it needs revision
3. What to study
4. Short revision tip

Keep the answer simple and concise.

INCORRECT QUESTIONS:

{wrong_text}
"""

    try:

        return generate_llm_response(
            prompt,
            max_tokens=500
        )

    except Exception as e:

        print(
            "Weak-topic analysis error:",
            e
        )

        return (
            "Weak-topic analysis is "
            "temporarily unavailable."
        )
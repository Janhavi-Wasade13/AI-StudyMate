import json

from rag import (
    extract_text_from_pdf,
    create_chunks,
    create_vector_database,
    retrieve_chunks,
    generate_answer,
    generate_mcqs
)


# ============================================================
# PDF PATH
# ============================================================

pdf_path = (
    "study_material/"
    "MACHINE LEARNING.pdf"
)


# ============================================================
# STEP 1: PDF EXTRACTION
# ============================================================

print("\n==============================")
print("STEP 1: PDF TEXT EXTRACTION")
print("==============================")

try:

    text = extract_text_from_pdf(
        pdf_path
    )

    print(
        "PDF text extracted successfully."
    )

    print(
        "Number of characters:",
        len(text)
    )

except Exception as e:

    print(
        "❌ PDF extraction failed:"
    )

    print(e)

    raise SystemExit


# ============================================================
# STEP 2: CREATE CHUNKS
# ============================================================

print("\n==============================")
print("STEP 2: CREATE CHUNKS")
print("==============================")

chunks = create_chunks(
    text
)

print(
    "Number of chunks:",
    len(chunks)
)


# ============================================================
# STEP 3: VECTOR DATABASE
# ============================================================

print("\n==============================")
print("STEP 3: VECTOR DATABASE")
print("==============================")

embedding_model, vector_db = (
    create_vector_database(
        chunks
    )
)

print(
    "Vector database created successfully."
)


# ============================================================
# STEP 4: QUESTION
# ============================================================

print("\n==============================")
print("STEP 4: QUESTION")
print("==============================")

question = (
    "What is overfitting?"
)

print(
    "Question:",
    question
)


# ============================================================
# STEP 5: RETRIEVAL
# ============================================================

print("\n==============================")
print("STEP 5: RETRIEVAL")
print("==============================")

relevant_chunks = retrieve_chunks(
    question,
    embedding_model,
    vector_db,
    chunks,
    k=3
)

print(
    "Retrieved chunks:",
    len(relevant_chunks)
)

for i, chunk in enumerate(
    relevant_chunks
):

    print(
        f"\n--- Chunk {i + 1} ---"
    )

    print(chunk)


# ============================================================
# STEP 6: AI ANSWER
# ============================================================

print("\n==============================")
print("STEP 6: AI ANSWER")
print("==============================")

answer = generate_answer(
    question,
    relevant_chunks
)

print("\nFinal Answer:")
print(answer)


# ============================================================
# STEP 7: MCQ GENERATION
# ============================================================

print("\n==============================")
print("STEP 7: MCQ GENERATION")
print("==============================")

mcqs_text = generate_mcqs(
    relevant_chunks,
    number_of_questions=5
)

print("\nMCQ response:")
print(mcqs_text)


# ============================================================
# STEP 8: MCQ VALIDATION
# ============================================================

print("\n==============================")
print("STEP 8: MCQ VALIDATION")
print("==============================")

try:

    mcqs = json.loads(
        mcqs_text
    )

    if len(mcqs) == 0:

        print(
            "❌ No valid MCQs generated."
        )

    else:

        print(
            f"✅ {len(mcqs)} MCQs generated."
        )

        for i, mcq in enumerate(
            mcqs
        ):

            print(
                f"\nQuestion {i + 1}:"
            )

            print(
                mcq["question"]
            )

            print(
                "A.",
                mcq["options"]["A"]
            )

            print(
                "B.",
                mcq["options"]["B"]
            )

            print(
                "C.",
                mcq["options"]["C"]
            )

            print(
                "D.",
                mcq["options"]["D"]
            )

            print(
                "Correct Answer:",
                mcq["answer"]
            )

            print(
                "Explanation:",
                mcq["explanation"]
            )

except json.JSONDecodeError:

    print(
        "❌ MCQ response is not valid JSON."
    )
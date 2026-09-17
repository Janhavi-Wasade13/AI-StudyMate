# 📚 AI StudyMate

**AI StudyMate** is an AI-powered study assistant that helps students learn from their own PDF study materials.

Students can upload a PDF, ask questions about the uploaded material, generate multiple-choice questions (MCQs), take a quiz, view their score, and identify topics that need revision.

---

## 🚀 Live Demo

**Streamlit App:** YOUR_STREAMLIT_APP_URL

**GitHub Repository:** YOUR_GITHUB_REPOSITORY_URL

---

## 💡 Problem Statement

Students often spend a lot of time searching through lengthy study materials and PDF notes to find specific information.

Traditional study methods also provide limited feedback about which topics a student needs to revise.

A student may know that they performed poorly in a quiz, but may not know exactly which concepts require more attention.

**AI StudyMate** addresses this problem by allowing students to interact directly with their study material and receive AI-powered answers, quizzes, and revision feedback.

---

## 🎯 Solution

AI StudyMate combines **Retrieval-Augmented Generation (RAG)** with an interactive quiz system.

The application follows these steps:

1. **Extracts text** from the uploaded PDF.
2. **Splits the text** into smaller chunks.
3. **Converts the chunks** into numerical embeddings.
4. **Stores the embeddings** in a FAISS vector index.
5. **Retrieves relevant chunks** when the student asks a question.
6. **Sends the retrieved context and question** to an LLM.
7. **Generates an AI-powered answer.**
8. **Generates MCQs** from the study material.
9. **Evaluates quiz performance.**
10. **Identifies weak areas** based on incorrect answers.

---

# ✨ Features

## 📄 1. PDF Study Material

Students can upload their study material in PDF format.

The application automatically:

- Extracts text from the PDF
- Processes the extracted content
- Splits the content into smaller chunks
- Creates embeddings for the chunks

---

## 💬 2. Ask Questions

Students can ask questions about their uploaded study material.

**Example:**

> What is overfitting?

The system searches the uploaded document for relevant information and generates an AI-powered answer.

---

## 🔎 3. Semantic Retrieval

AI StudyMate uses **embedding-based semantic retrieval** instead of relying only on exact keyword matching.

For example, suppose the PDF contains:

> A model performs poorly on previously unseen data.

The student asks:

> Why does the model fail on new data?

Even though the exact words are different, the meaning is related.

The embedding-based retrieval system can identify the relevant content.

---

## 📝 4. MCQ Generation

AI StudyMate can automatically generate multiple-choice questions from the study material.

Students can select between **3 and 10 questions**.

Each MCQ contains:

- **Question**
- **Four options**
- **Correct answer**
- **Explanation**

---

## 🎯 5. Interactive Quiz

Students can attempt the generated MCQs directly inside the application.

After submitting the quiz, the application calculates:

- **Total score**
- **Accuracy percentage**
- **Correct answers**
- **Incorrect answers**

🔍 6. Weak Area Analysis

AI StudyMate analyzes incorrectly answered questions.

It identifies the concepts associated with incorrect answers and provides revision suggestions.

Example:

Weak Topics:

- Types of Machine Learning
- Normalization Methods

Revision Suggestion:

Review the different types of machine learning
and normalization techniques.
📖 7. Answer Review

After completing the quiz, students can review their answers.

For incorrect questions, the application displays:

The question
The correct answer
Explanation

This helps students understand their mistakes rather than only seeing their score.

🧠 How RAG Works

AI StudyMate uses Retrieval-Augmented Generation (RAG).

The complete pipeline is:

PDF Upload
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Text Embeddings
    ↓
FAISS Vector Index
    ↓
Student Question
    ↓
Question Embedding
    ↓
Similarity Search
    ↓
Relevant Document Chunks
    ↓
Large Language Model
    ↓
Final Answer
🔹 What is RAG?

RAG stands for Retrieval-Augmented Generation.

It combines two main processes.

Retrieval

The system searches the uploaded study material and retrieves the most relevant text chunks.

Generation

The retrieved information is provided as context to the Large Language Model, which generates the final response.

This allows AI StudyMate to answer questions using the student's uploaded study material.

🧩 Chunking

Large documents are divided into smaller pieces called chunks.

AI StudyMate currently uses:

chunk_size = 1000
chunk_overlap = 100

This means each chunk contains approximately 1000 characters, while approximately 100 characters are shared between consecutive chunks.

The overlap helps preserve context when important information crosses chunk boundaries.

🔢 Embeddings

Embeddings convert text into numerical vectors that represent the semantic meaning of the text.

AI StudyMate uses:

sentence-transformers/all-MiniLM-L6-v2

For example:

"What is overfitting?"

is converted into a numerical vector.

The document chunks are also converted into numerical vectors.

The vectors can then be compared to find semantically relevant content.

🗄️ Vector Search with FAISS

AI StudyMate uses FAISS for vector similarity search.

FAISS stores the embeddings of the document chunks and allows the application to search for relevant chunks.

The current retrieval process uses:

Top-K = 3

This means the system retrieves the three most relevant chunks for a question.

Important Distinction
Semantic search = retrieval approach
Embeddings = numerical representations of text meaning
FAISS = vector-search library used to compare embeddings

The current implementation uses:

FAISS IndexFlatL2

which compares vectors using L2 (Euclidean) distance.

🤖 Large Language Model

AI StudyMate uses a Large Language Model through the Hugging Face Inference API.

The LLM receives:

Original Question
        +
Retrieved Document Context

The model then generates the final answer based on the retrieved context.

🛠️ Technology Stack
Technology	Purpose
Python	Programming language
Streamlit	Web application interface
PyPDF	PDF text extraction
LangChain Text Splitters	Text chunking
Sentence Transformers	Text embeddings
all-MiniLM-L6-v2	Embedding model
FAISS	Vector similarity search
Hugging Face	LLM inference
DeepSeek-V3	Large Language Model
python-dotenv	Environment variable management
Git	Version control
GitHub	Source code hosting
Streamlit Community Cloud	Deployment
📂 Project Structure
AI-StudyMate/
│
├── app.py
├── rag.py
├── test-rag.py
├── test_hf.py
├── requirements.txt
├── .gitignore
│
└── study_material/
Main Files
app.py

Contains the Streamlit user interface and application workflow.

rag.py

Contains the core RAG pipeline including:

PDF extraction
Chunking
Embeddings
FAISS vector search
Retrieval
LLM response generation
MCQ generation
Weak-topic analysis
test-rag.py

Tests the main RAG pipeline.

test_hf.py

Used to test Hugging Face API connectivity.

⚙️ Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Navigate to the Project
cd AI-StudyMate
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment
Windows
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
🔐 Environment Variables

Create a .env file in the project directory.

Add:

HF_TOKEN=your_hugging_face_token

The Hugging Face token is required to access the LLM through the Hugging Face Inference API.

Security

API keys and tokens should never be committed to GitHub.

The .gitignore file prevents sensitive files such as .env from being uploaded.

For Streamlit Cloud deployment, the Hugging Face token is stored securely using Streamlit Secrets.

▶️ Run Locally

Start the Streamlit application using:

streamlit run app.py

The application will open in your browser.

🧪 Testing

The RAG pipeline can be tested using:

python test-rag.py

The test verifies:

PDF text extraction
Text chunking
Embedding generation
FAISS vector database creation
Semantic retrieval
AI answer generation
MCQ generation
📊 Example Workflow
Upload PDF
     ↓
Study Material Processed
     ↓
Ask a Question
     ↓
Relevant Content Retrieved
     ↓
AI Generates Answer
     ↓
Generate MCQs
     ↓
Attempt Quiz
     ↓
Submit Quiz
     ↓
View Score & Accuracy
     ↓
Identify Weak Topics
     ↓
Revise
🎓 Example Use Case

Suppose a student uploads a Machine Learning PDF.

The student asks:

What is overfitting?

AI StudyMate searches the document for relevant information and generates an answer.

The student can then generate MCQs from the study material.

After completing the quiz, the application might display:

Score: 3/5
Accuracy: 60%

The application then analyzes the incorrect answers and identifies topics that require revision.

This creates a simple learning cycle:

Learn
  ↓
Ask
  ↓
Practice
  ↓
Test
  ↓
Identify Weak Areas
  ↓
Revise
🔒 Responsible AI

AI StudyMate uses AI-assisted generation while grounding responses in the uploaded study material.

The system:

Retrieves relevant information from the study material.
Provides retrieved content as context to the LLM.
Instructs the model to use the provided context.
Provides a fallback when information cannot be found.
Keeps API credentials outside the source code.
Uses Streamlit Secrets for the deployed application.

AI-generated content should still be reviewed by students, especially when used for important academic decisions.

🌍 Use Cases

AI StudyMate can be used for:

College exam preparation
Technical subjects
Revision from lecture notes
PDF-based learning
Self-assessment
Quick question answering
MCQ practice
Identifying topics requiring revision
🔮 Future Improvements

Possible future improvements include:

Multiple PDF support
Topic-wise progress tracking
Personalized study plans
Difficulty-level selection for MCQs
More advanced retrieval techniques
Improved learning analytics
Personalized revision schedules
Better quiz question diversity
👩‍💻 Author
Janhavi

B.Tech Computer Science and Engineering Student

Areas of Interest
Machine Learning
Generative AI
Retrieval-Augmented Generation
Data Structures & Algorithms
Artificial Intelligence
📜 License

This project is created for educational and hackathon purposes.

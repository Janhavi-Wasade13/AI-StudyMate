# 📚 AI StudyMate

AI StudyMate is an AI-powered study assistant that helps students learn from their own PDF study materials.

Students can upload a PDF, ask questions about the uploaded material, generate multiple-choice questions (MCQs), take a quiz, view their score, and identify topics that need revision.

## 🚀 Live Demo

🔗 **Streamlit App:**  
https://ai-studymate-co9yxx5qe6xwyuiu287fop.streamlit.app/

## 💡 Problem Statement

Students often spend a lot of time searching through lengthy notes and PDFs to find specific information. Traditional study methods also provide limited feedback about which topics a student needs to revise.

AI StudyMate addresses this problem by allowing students to interact with their study material through an AI-powered question-answering and quiz system.

## 🎯 Solution

AI StudyMate uses Retrieval-Augmented Generation (RAG) to answer questions using information from the student's uploaded PDF.

The application also generates MCQs from the study material and evaluates the student's answers.

Based on incorrect answers, the application provides a weak-topic analysis and revision suggestions.

## ✨ Features

### 📄 PDF Study Material
- Upload study material in PDF format.
- Extract text automatically from the PDF.
- Split the extracted text into smaller chunks.

### 💬 Ask Questions
- Ask questions about the uploaded study material.
- Uses semantic search to retrieve relevant information.
- Generates answers using an AI language model.
- Answers are grounded in retrieved document content.

### 📝 MCQ Generation
- Automatically generates multiple-choice questions.
- Supports 3–10 questions per quiz.
- Provides four answer options.
- Provides the correct answer and explanation.

### 🎯 Quiz System
- Students can attempt generated MCQs.
- Automatically evaluates answers.
- Calculates the quiz score.
- Displays accuracy percentage.

### 🔍 Weak Topic Analysis
- Identifies questions answered incorrectly.
- Analyzes the concepts associated with incorrect answers.
- Provides revision suggestions.

### 📖 Answer Review
- Shows which questions were answered correctly or incorrectly.
- Displays the correct answer.
- Provides explanations for incorrect answers.

## 🧠 How RAG Works

AI StudyMate follows a Retrieval-Augmented Generation pipeline:

```text
PDF Upload
    ↓
Text Extraction
    ↓
Text Chunking
    ↓
Text Embeddings
    ↓
FAISS Vector Database
    ↓
Student Question
    ↓
Question Embedding
    ↓
Semantic Similarity Search
    ↓
Relevant Document Chunks
    ↓
LLM
    ↓
Final Answer
🔹 What is RAG?

RAG stands for:

Retrieval-Augmented Generation

It combines two main processes:

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

This means each chunk contains approximately 1000 characters, with approximately 100 characters overlapping between consecutive chunks.

The overlap helps preserve context when important information crosses chunk boundaries.

🔢 Embeddings

Embeddings convert text into numerical vectors that represent the semantic meaning of the text.

AI StudyMate uses:

sentence-transformers/all-MiniLM-L6-v2

For example:

"What is overfitting?"

is converted into a numerical vector.

The same process is applied to document chunks.

The vectors can then be compared to find semantically similar content.

🗄️ Vector Database

AI StudyMate uses FAISS for vector similarity search.

FAISS stores the embeddings of the document chunks and allows the application to efficiently search for relevant chunks.

The current retrieval process uses:

Top-K = 3

This means the system retrieves the three most relevant chunks for a question.

🤖 Large Language Model

AI StudyMate uses a Large Language Model through the Hugging Face Inference API.

The LLM receives:

Original Question
        +
Retrieved Document Context

and generates the final response.

The application instructs the model to use the provided context when answering questions.

🛠️ Technology Stack
Programming Language
Python
Frontend
Streamlit
PDF Processing
PyPDF
Text Processing
LangChain Text Splitters
Embeddings
Hugging Face
Sentence Transformers
all-MiniLM-L6-v2
Vector Database
FAISS
LLM
Hugging Face Inference API
DeepSeek-V3
Environment Management
Python-dotenv
Deployment
Streamlit Community Cloud
Version Control
Git
GitHub
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

The Hugging Face token is required for the LLM API.

Security

API keys and tokens should never be committed to GitHub.

The .gitignore file prevents sensitive files such as .env from being uploaded.

For Streamlit Cloud deployment, the Hugging Face token is stored securely using Streamlit Secrets.

▶️ Run Locally

Start the application using:

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

A typical user workflow looks like this:

1. Upload PDF
       ↓
2. Study material is processed
       ↓
3. Ask a question
       ↓
4. Relevant content is retrieved
       ↓
5. AI generates an answer
       ↓
6. Generate MCQs
       ↓
7. Attempt quiz
       ↓
8. Submit quiz
       ↓
9. View score and accuracy
       ↓
10. Review weak topics
🎓 Example Use Case

Suppose a student uploads a Machine Learning PDF.

The student asks:

What is overfitting?

AI StudyMate searches the document for relevant information and generates an answer.

The student can then generate MCQs related to the study material.

After completing the quiz, the application might display:

Score: 3/5
Accuracy: 60%

The system then identifies the topics associated with incorrect answers and provides revision suggestions.

This creates a simple learning loop:

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

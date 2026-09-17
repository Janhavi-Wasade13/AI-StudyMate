# 📚 AI StudyMate

AI StudyMate is an AI-powered study assistant that helps students learn from their own PDF study materials.

Students can upload a PDF, ask questions about the uploaded material, generate multiple-choice questions (MCQs), take a quiz, view their score, and identify topics that need revision.

## 🚀 Live Demo

🔗 **Streamlit App:**  
PASTE_YOUR_STREAMLIT_APP_LINK_HERE

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

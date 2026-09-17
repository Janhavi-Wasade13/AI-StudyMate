###📚 AI StudyMate
AI-powered study assistant using RAG, semantic retrieval, MCQ generation, and quiz-based weak-area analysis.
###🚀 Live Demo
Streamlit App: https://ai-studymate-co9yxx5qe6xwyuiu287fop.streamlit.app/
GitHub Repository: https://github.com/Janhavi-Wasade13/AI-StudyMate
###💡 Problem Statement
Students often spend a lot of time searching through lengthy study materials and PDF notes to find specific information. Traditional study methods also provide limited feedback about which topics a student needs to revise. AI StudyMate addresses this problem by allowing students to interact directly with their study material and receive AI-powered answers, quizzes, and revision feedback.
###🎯 Solution
AI StudyMate combines Retrieval-Augmented Generation (RAG) with an interactive quiz system. The student uploads a PDF containing study material. The application extracts and chunks the text, creates embeddings, stores them in a FAISS vector index, retrieves relevant chunks for questions, sends the retrieved context to an LLM, generates answers and MCQs, evaluates quiz performance, and analyzes incorrect answers to identify areas for revision.
###✨ Features
###📄 PDF Study Material
•	Upload study material in PDF format.
•	Extract text automatically from the PDF.
•	Split extracted text into smaller chunks.
•	Create embeddings for retrieval.
###💬 Ask Questions
•	Ask questions about the uploaded study material.
•	Retrieve relevant document chunks using embedding-based similarity search.
•	Generate an AI-powered answer using the retrieved context.
###🔎 Semantic Retrieval
•	The system represents document chunks and the user's question as embeddings.
•	FAISS compares the question vector with document vectors and retrieves the closest chunks.
•	Because embeddings capture semantic meaning, the system can retrieve related content even when the wording is not identical.
###📝 MCQ Generation
•	Generate 3–10 multiple-choice questions.
•	Each question contains four options.
•	Provide the correct answer and explanation.
###🎯 Interactive Quiz
•	Attempt generated MCQs inside the application.
•	Automatically calculate score and accuracy.
•	Identify correct and incorrect answers.
###🔍 Weak Area Analysis
•	Analyze incorrectly answered questions.
•	Identify concepts associated with mistakes.
•	Provide revision suggestions.
###📖 Answer Review
•	Review correct and incorrect answers.
•	Show the correct answer and explanation for incorrect responses.
###🧠 Why Semantic Search?
AI StudyMate uses embedding-based similarity retrieval rather than simple keyword matching. The reason is that students may ask a question using different words from those used in the PDF. Embeddings convert text into numerical vectors that represent semantic meaning. FAISS then finds document vectors that are close to the question vector.
Example:
PDF: "A model performs poorly on previously unseen data."
Question: "Why does the model fail on new data?"
The wording is different, but the meaning is related. Embedding-based retrieval can therefore retrieve the relevant chunk. In the current implementation, FAISS uses IndexFlatL2, which measures L2 (Euclidean) distance between vectors. So the project is accurately described as semantic or embedding-based retrieval; it is not simply exact keyword search.
Important distinction: semantic search is the retrieval approach; FAISS is the vector-search library/index used to perform that retrieval.
###🧠 How RAG Works
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
###🔹 What is RAG?
RAG stands for Retrieval-Augmented Generation. It combines retrieval and generation. Retrieval finds relevant information from the uploaded study material. Generation uses an LLM to produce the final response from the retrieved context and the student's question.
###🧩 Chunking
Large documents are divided into smaller pieces called chunks. AI StudyMate currently uses a chunk size of approximately 1000 characters and an overlap of approximately 100 characters.
chunk_size = 1000
chunk_overlap = 100
The overlap helps preserve context when information crosses the boundary between two chunks.
###🔢 Embeddings
Embeddings convert text into numerical vectors that capture aspects of its semantic meaning. AI StudyMate uses the sentence-transformers/all-MiniLM-L6-v2 embedding model.
sentence-transformers/all-MiniLM-L6-v2
###🗄️ Vector Database / FAISS
AI StudyMate uses FAISS to store document vectors and perform similarity search. The current implementation uses FAISS IndexFlatL2. For each user question, the question is embedded and compared against the stored document vectors. The closest results are retrieved.
Top-K = 3
Top-K = 3 means the application retrieves the three closest document chunks for the question.
###🤖 Large Language Model
AI StudyMate uses a Large Language Model through the Hugging Face Inference API. The LLM receives the original question together with the retrieved document context and generates the final response.
###🛠️ Technology Stack
•	Python
•	Streamlit
•	PyPDF
•	LangChain Text Splitters
•	Hugging Face
•	Sentence Transformers
•	all-MiniLM-L6-v2
•	FAISS
•	Hugging Face Inference API
•	DeepSeek-V3
•	python-dotenv
•	Streamlit Community Cloud
•	Git and GitHub
###📂 Project Structure
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
###⚙️ Installation
1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL
2. Navigate to the Project
cd AI-StudyMate
3. Create a Virtual Environment
python -m venv venv
4. Activate the Virtual Environment — Windows
venv\Scripts\activate
5. Install Dependencies
pip install -r requirements.txt
###🔐 Environment Variables
Create a .env file locally and add:
HF_TOKEN=your_hugging_face_token
Never commit API keys or tokens to GitHub. The .gitignore file excludes .env. For Streamlit Cloud, the Hugging Face token is stored using Streamlit Secrets.
###▶️ Run Locally
streamlit run app.py
###🧪 Testing
python test-rag.py
The test verifies PDF text extraction, text chunking, embedding generation, FAISS vector database creation, semantic retrieval, AI answer generation, and MCQ generation.
###📊 Example Workflow
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
###🎓 Example Use Case
A student uploads a Machine Learning PDF and asks, 'What is overfitting?' The application retrieves relevant content from the document and generates an answer. The student can then generate MCQs, attempt the quiz, view the score and accuracy, and review the concepts associated with incorrect answers.
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
###🔒 Responsible AI
•	Uses retrieved study-material content as context for question answering.
•	Instructs the LLM to use the provided context.
•	Provides a fallback when information cannot be found.
•	Keeps API credentials outside source code.
•	Uses Streamlit Secrets for the deployed application.
•	AI-generated content should still be reviewed by students for important academic decisions.
###🌍 Use Cases
•	College exam preparation
•	Technical subjects
•	Revision from lecture notes
•	PDF-based learning
•	Self-assessment
•	Quick question answering
•	MCQ practice
•	Identifying topics requiring revision
###🔮 Future Improvements
•	Multiple PDF support
•	Topic-wise progress tracking
•	Personalized study plans
•	Difficulty-level selection for MCQs
•	More advanced retrieval techniques
•	Improved learning analytics
•	Personalized revision schedules
•	Better quiz question diversity
###👩‍💻 Author
Janhavi
B.Tech Computer Science and Engineering Student
Areas of Interest:
•	Machine Learning
•	Generative AI
•	Retrieval-Augmented Generation
•	Data Structures & Algorithms
•	Artificial Intelligence
###📜 License
This project is created for educational and hackathon purposes.

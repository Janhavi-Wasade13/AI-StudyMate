import json

import streamlit as st

from rag import (
    extract_text_from_pdf,
    create_chunks,
    create_vector_database,
    retrieve_chunks,
    generate_answer,
    generate_mcqs,
    analyze_weak_topics
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI StudyMate",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title(
    "📚 AI StudyMate"
)

st.write(
    "Upload your study material, ask questions, "
    "generate MCQs, test yourself, and identify "
    "topics that need revision."
)


# ============================================================
# PDF UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "Upload your study material (PDF)",
    type=["pdf"]
)


if uploaded_file is not None:

    pdf_path = "uploaded.pdf"


    # ========================================================
    # SAVE PDF
    # ========================================================

    with open(
        pdf_path,
        "wb"
    ) as file:

        file.write(
            uploaded_file.getbuffer()
        )


    # ========================================================
    # PROCESS PDF
    # ========================================================

    with st.spinner(
        "Processing your PDF..."
    ):

        text = extract_text_from_pdf(
            pdf_path
        )

        chunks = create_chunks(
            text
        )

        embedding_model, vector_db = (
            create_vector_database(
                chunks
            )
        )


    st.success(
        "✅ Study material processed successfully!"
    )

    st.write(
        f"📄 Characters extracted: {len(text)}"
    )

    st.write(
        f"🧩 Chunks created: {len(chunks)}"
    )


    # ========================================================
    # ASK QUESTIONS
    # ========================================================

    st.header(
        "💬 Ask Your Study Material"
    )

    question = st.text_input(
        "Enter your question:"
    )


    if st.button(
        "Get Answer"
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Finding the answer..."
            ):

                relevant_chunks = (
                    retrieve_chunks(
                        question,
                        embedding_model,
                        vector_db,
                        chunks,
                        k=3
                    )
                )

                answer = generate_answer(
                    question,
                    relevant_chunks
                )


            st.subheader(
                "🤖 Answer"
            )

            st.write(
                answer
            )


    # ========================================================
    # MCQ GENERATION
    # ========================================================

    st.header(
        "📝 Generate MCQs"
    )

    number_of_questions = st.slider(
        "Number of questions",
        min_value=3,
        max_value=10,
        value=5
    )


    if st.button(
        "Generate MCQs"
    ):

        if not chunks:

            st.error(
                "No study material was found."
            )

        else:

            quiz_chunks = chunks[:8]


            with st.spinner(
                "Generating MCQs..."
            ):

                mcqs_text = generate_mcqs(
                    quiz_chunks,
                    number_of_questions
                )


            try:

                mcqs = json.loads(
                    mcqs_text
                )

            except json.JSONDecodeError:

                st.error(
                    "The AI returned an invalid "
                    "MCQ format. Please try again."
                )

                st.stop()


            if not isinstance(
                mcqs,
                list
            ) or len(mcqs) == 0:

                st.error(
                    "No MCQs were generated."
                )

            else:

                st.session_state[
                    "mcqs"
                ] = mcqs

                st.session_state[
                    "quiz_submitted"
                ] = False

                st.session_state[
                    "score"
                ] = None

                st.session_state[
                    "wrong_questions"
                ] = []

                st.session_state[
                    "user_answers"
                ] = {}

                st.success(
                    f"✅ {len(mcqs)} MCQs "
                    "generated successfully!"
                )


    # ========================================================
    # QUIZ
    # ========================================================

    if (
        "mcqs" in st.session_state
        and st.session_state["mcqs"]
    ):

        mcqs = st.session_state[
            "mcqs"
        ]


        st.header(
            "🎯 Take the Quiz"
        )


        user_answers = {}


        for i, mcq in enumerate(
            mcqs
        ):

            st.subheader(
                f"Question {i + 1}"
            )

            st.write(
                mcq["question"]
            )

            options = mcq["options"]


            user_answers[i] = st.radio(
                "Choose your answer:",

                ["A", "B", "C", "D"],

                format_func=lambda x,
                options=options:
                    f"{x}. {options[x]}",

                key=f"question_{i}"
            )


        # ====================================================
        # SUBMIT QUIZ
        # ====================================================

        if st.button(
            "Submit Quiz"
        ):

            score = 0

            wrong_questions = []


            for i, mcq in enumerate(
                mcqs
            ):

                if (
                    user_answers[i]
                    == mcq["answer"]
                ):

                    score += 1

                else:

                    wrong_questions.append(
                        mcq
                    )


            st.session_state[
                "score"
            ] = score

            st.session_state[
                "wrong_questions"
            ] = wrong_questions

            st.session_state[
                "user_answers"
            ] = user_answers

            st.session_state[
                "quiz_submitted"
            ] = True


    # ========================================================
    # PERFORMANCE
    # ========================================================

    if st.session_state.get(
        "quiz_submitted",
        False
    ):

        mcqs = st.session_state[
            "mcqs"
        ]

        score = st.session_state[
            "score"
        ]

        wrong_questions = (
            st.session_state[
                "wrong_questions"
            ]
        )

        user_answers = (
            st.session_state[
                "user_answers"
            ]
        )


        st.header(
            "📊 Your Performance"
        )


        total_questions = len(
            mcqs
        )


        percentage = (
            score / total_questions
        ) * 100


        st.success(
            f"🎉 Your Score: "
            f"{score}/{total_questions}"
        )


        st.write(
            f"**Accuracy: "
            f"{percentage:.1f}%**"
        )


        # ====================================================
        # WEAK AREA ANALYSIS
        # ====================================================

        if not wrong_questions:

            st.success(
                "🏆 Excellent! "
                "You answered all questions correctly."
            )

        else:

            st.warning(
                f"⚠️ You got "
                f"{len(wrong_questions)} "
                "question(s) wrong."
            )


            st.subheader(
                "🔍 Weak Area Analysis"
            )


            with st.spinner(
                "Analyzing your weak areas..."
            ):

                analysis = (
                    analyze_weak_topics(
                        wrong_questions
                    )
                )


            st.write(
                analysis
            )


        # ====================================================
        # ANSWER REVIEW
        # ====================================================

        st.header(
            "📖 Answer Review"
        )


        for i, mcq in enumerate(
            mcqs
        ):

            correct_answer = (
                mcq["answer"]
            )


            if (
                user_answers[i]
                == correct_answer
            ):

                st.write(
                    f"✅ Question {i + 1}: "
                    "Correct"
                )

            else:

                st.write(
                    f"❌ Question {i + 1}: "
                    "Incorrect"
                )

                st.write(
                    f"**Correct Answer:** "
                    f"{correct_answer}. "
                    f"{mcq['options'][correct_answer]}"
                )

                st.write(
                    f"**Explanation:** "
                    f"{mcq['explanation']}"
                )


else:

    st.info(
        "👆 Upload a PDF to start using AI StudyMate."
    )
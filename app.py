import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="AI Resume Assistant",
    page_icon="📄"
)

client = InferenceClient(token=os.getenv("HF_TOKEN"))

st.title("📄 AI Resume Assistant")
st.write("Improve your resume with AI assistance.")

st.subheader("📝 Enter Your Resume Details")

name = st.text_input("Your Name")

education = st.text_area(
    "Education",
    placeholder="Example: BE in Information Science Engineering"
)

skills = st.text_area(
    "Skills",
    placeholder="Example: Python, SQL, HTML, CSS"
)

experience = st.text_area(
    "Experience / Internships",
    placeholder="Example: AI internship at Skyrovix"
)

projects = st.text_area(
    "Projects",
    placeholder="Example: AI Chatbot, Language Translation Tool"
)

job_role = st.text_input(
    "Target Job Role",
    placeholder="Example: Software Engineer"
)

# Store conversation history for context handling
if "resume_context" not in st.session_state:
    st.session_state.resume_context = []

if st.button("✨ Improve My Resume"):

    if not name or not job_role:
        st.warning("Please enter your name and target job role.")

    else:
        prompt = f"""
You are an AI Resume Assistant.

Help the user improve their resume for the target job role.

User details:
Name: {name}
Education: {education}
Skills: {skills}
Experience: {experience}
Projects: {projects}
Target Job Role: {job_role}

Give practical and professional suggestions.
Improve the wording where necessary.
Do not invent qualifications, experience, skills, or achievements.
Keep the suggestions clear and suitable for a student or entry-level applicant.
"""

        with st.spinner("AI is analyzing your resume..."):

            response = client.chat_completion(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a professional AI Resume Assistant. "
                            "Give clear, honest and practical resume suggestions."
                        )
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=600,
                temperature=0.7
            )

            answer = response.choices[0].message.content

        # Save the resume information as context
        st.session_state.resume_context = [
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "assistant",
                "content": answer
            }
        ]

        st.subheader("🤖 AI Resume Suggestions")
        st.write(answer)


# Follow-up section
if st.session_state.resume_context:

    st.divider()
    st.subheader("💬 Ask a Follow-up Question")

    follow_up = st.text_input(
        "Ask something about your resume",
        placeholder="Example: How can I improve my skills section?"
    )

    if st.button("Ask AI") and follow_up:

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a professional AI Resume Assistant. "
                    "Use the previous resume information to answer "
                    "follow-up questions accurately. "
                    "Do not invent qualifications or experience."
                )
            }
        ]

        messages.extend(st.session_state.resume_context)

        messages.append(
            {
                "role": "user",
                "content": follow_up
            }
        )

        with st.spinner("AI is thinking..."):

            response = client.chat_completion(
                model="openai/gpt-oss-120b",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )

            follow_up_answer = response.choices[0].message.content

        st.session_state.resume_context.append(
            {
                "role": "user",
                "content": follow_up
            }
        )

        st.session_state.resume_context.append(
            {
                "role": "assistant",
                "content": follow_up_answer
            }
        )

        st.subheader("🤖 AI Response")
        st.write(follow_up_answer)
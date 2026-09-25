# 📄 AI Resume Assistant

An AI-powered Resume Assistant developed as part of my 2-month Generative AI Internship at Skyrovix.

## 🎯 Project Overview

The AI Resume Assistant helps students and entry-level applicants improve their resumes using Generative AI.

Users can enter their education, skills, internships, projects, and target job role. The AI analyzes the information and provides professional resume suggestions.

The application also supports follow-up questions by maintaining the user's resume context during the session.

## ✨ Features

- Resume information input
- AI-powered resume suggestions
- Target job role-based recommendations
- Prompt design
- AI API integration
- Context handling
- Follow-up questions
- Response generation
- Simple Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Hugging Face Inference API
- Hugging Face InferenceClient
- Generative AI
- Prompt Engineering

## 🔄 Workflow

1. User enters resume details.
2. User provides the target job role.
3. The application creates a structured prompt.
4. The prompt is sent to the AI model through the Hugging Face Inference API.
5. The AI generates resume improvement suggestions.
6. The application stores the conversation context.
7. The user can ask follow-up questions based on the same resume information.

## 🧠 Prompt Design

The application uses a structured prompt containing:

- Education
- Skills
- Experience / Internships
- Projects
- Target job role

The AI is instructed to provide practical suggestions without inventing qualifications or experience.

## 🧪 Testing

The application was tested for:

- Required field validation
- AI response generation
- Resume improvement suggestions
- Follow-up questions
- Context handling
- Target job role-based suggestions

## 📌 Project Status

Completed as part of Task 2 of the Skyrovix Generative AI Internship.

## 🚀 Future Improvements

- Resume PDF upload
- Automatic resume formatting
- Resume scoring
- Job description matching
- Downloadable improved resume
- More advanced resume analysis

## 👩‍💻 Internship

**Internship:** Generative AI Internship  
**Organization:** Skyrovix  
**Task:** Task 2 – AI Resume Assistant
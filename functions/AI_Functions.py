import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") or "AIzaSyAswb8zCjcotAY9EkfDfpvP_BanFk0ui0c"

LLM = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.8,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GOOGLE_API_KEY
)

def generate_enhanced_resume(job_text, resume_text):
    prompt_template = ChatPromptTemplate([
        (
            "system",
            (
                "You are an expert AI resume writer trained in creating high-conversion, ATS-optimized resumes for top tech jobs. "
                "Your task is to take an original resume and a job description, and rewrite the resume to significantly increase its alignment with the job role. "
                "Focus on highlighting relevant experience, optimizing keywords, and improving phrasing to sound more impactful and professional. "
                "You are allowed to make creative additions such as inferred skills, tools, or achievements if they match the candidate’s domain and align with the job description. "
                "Rewrite the resume in HTML format using the following structure: "
                "1. Name and Contact (retain from original), "
                "2. Professional Summary (highly tailored to the job), "
                "3. Key Skills (expanded and matched to job), "
                "4. Experience (reworded, reordered, and enhanced with job-relevant points, make it into an array of points with the following fields title: string; company: string; dates: string; description: string[];), "
                "5. Projects (add a relevant project according to the job description if the project mentioned is not in the required skills), "
                "6. Education (return as an array of objects with these fields: institution (string), degree (string), dates (string), cgpa (string), percentage (string)), "
                "7. Certifications (if any), "
                "8. Job Role (if any). "
                "9. Hobbies (if any). "
                "10. Languages (if any). "
                "Job Description: {job_text} "
                "Output only the improved resume in JSON format with the keys as follows: "
                "name (string), job_role (string), mobile (string), email (string), linkedin (string), github (string), professional_summary (string), key_skills (array of strings), "
                "experience (array with fields: title (string), company (string), dates (string), description (array of strings)), "
                "projects (array with fields: title (string), description (array of strings), tech_stack (string)), "
                "education (array with fields: institution (string), degree (string), dates (string), cgpa (string), percentage (string)), "
                "certifications (array with fields: title (string), date (string), organization (string)). "
                "hobbies (array of strings), languages (array of strings). "
                "All these fields must be present in the output JSON. If no data is present for a field, use an empty array or empty string."
            )
        ),
        ("user", "Original Resume: {resume_text}"),
    ])
    prompt = prompt_template.invoke({"job_text" : job_text, "resume_text" : resume_text})
    ai_response = LLM.invoke(prompt)
    return ai_response.content
 
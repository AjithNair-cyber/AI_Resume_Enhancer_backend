import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

LLM = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.8,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    google_api_key=GOOGLE_API_KEY
)

def generate_enhanced_resume(job_text, resume_text):
    prompt_template = ChatPromptTemplate(
    [("system", "You are an expert AI resume writer trained in creating high-conversion, ATS-optimized resumes for top tech jobs. "
    "Your task is to take an original resume and a job description, and rewrite the resume to significantly increase its alignment with the job role. "
    "Focus on highlighting relevant experience, optimizing keywords, and improving phrasing to sound more impactful and professional. "
    "You are allowed to make creative additions such as inferred skills, tools, or achievements if they match the candidate’s domain and align with the job description. "
    "Rewrite the resume in HTML format using the following structure: "
    "1. Name and Contact (retain from original), "
    "2. Professional Summary (highly tailored to the job), "
    "3. Key Skills (expanded and matched to job), "
    "4. Experience (reworded, reordered, and enhanced with job-relevant points), "
    "5. Education, "
    "6. Certifications (if any). "
    "Job Description: {job_text} "
    "Output only the improved resume in clean HTML — no commentary or explanation."),
    ("user", "Original Resume: {resume_text}"),
    ])
    prompt = prompt_template.invoke({"job_text" : job_text, "resume_text" : resume_text})
    ai_response = LLM.invoke(prompt)
    return ai_response.content
 
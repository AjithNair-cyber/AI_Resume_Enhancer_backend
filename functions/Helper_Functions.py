from flask import jsonify
import bcrypt
import jwt
import datetime


SECRET = "iPXioyQ67t2anHUEsmdzDCBgv"

def clean_json_output(text: str) -> str:
    # Remove leading/trailing markdown backticks and 'json'
    if text.strip().startswith("```json"):
        text = text.strip()[7:]  # remove ```json
    if text.strip().endswith("```"):
        text = text.strip()[:-3]  # remove trailing ```
    return text.strip()

def success_response_formatter(data):
    return jsonify({
        "success": "true",
        "data" : data
    })

def error_response_formatter(data, status):
    return jsonify({
        "success": "false",
        "data" : data
    }), status

def generate_password_hash(raw_password):
    password = raw_password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt).decode('utf-8')

def compare_password_hash(password, hashed_password):
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        return True
    else:
        return False

def generate_jwt(user):
    
    # Define the expiry time (e.g., 1 hour from now)
    expiration_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)

    # Convert the datetime object to a Unix timestamp
    expiration_timestamp = int(expiration_time.timestamp())

    payload = {
        "email" : user["email"],
        "username" : user["name"],
        "exp" : expiration_timestamp
    }

    encoded_jwt = jwt.encode(payload, SECRET, algorithm="HS256")
    return encoded_jwt

def decode_jwt(jwt_token):
  try:
    user = jwt.decode(jwt_token, SECRET, algorithms=["HS256"])
    return user
  except Exception as e:
    return False

def return_dummy_data() :
    return {
  "name": "Ajith Nair",
  "job_role": "Full Stack Developer",
  "mobile": "+91-9876543210",
  "email": "ajith.nair@example.com",
  "linkedin": "https://linkedin.com/in/ajithnair",
  "github": "https://github.com/ajithnair",
  "professional_summary": "Results-driven Full Stack Developer with 3+ years of experience building scalable web applications using React, Node.js, and PostgreSQL. Proven track record of designing and deploying secure, high-performance software solutions in Agile environments. Passionate about clean code, DevOps automation, and continuous learning, with a strong foundation in cloud technologies and CI/CD practices.",
  "key_skills": [
    "React.js",
    "Node.js",
    "Express.js",
    "PostgreSQL",
    "MongoDB",
    "Docker",
    "Azure DevOps",
    "REST APIs",
    "CI/CD",
    "Unit Testing",
    "Agile Development",
    "Git",
    "HTML5",
    "CSS3",
    "TypeScript"
  ],
  "experience": [
    {
      "title": "Full Stack Developer",
      "company": "TechNova Solutions",
      "start_date": "",
      "end_date": "Present",
      "description": [
        "Developed and maintained a logistics tracking system using React, Node.js, and PostgreSQL, improving shipment visibility by 45%.",
        "Integrated Azure DevOps pipelines for CI/CD, reducing deployment time by 60%.",
        "Optimized MongoDB queries, resulting in 30% faster data retrieval.",
        "Led migration from REST to GraphQL APIs, enhancing front-end flexibility and backend performance.",
        "Collaborated with cross-functional teams using Agile methodologies and participated in weekly sprint reviews."
      ]
    },
    {
      "title": "Software Developer Intern",
      "company": "InnovaTech Pvt Ltd",
      "start_date": "Jan 2021",
      "end_date": "June 2022",
      "description": [
        "Built responsive UI components using React and TailwindCSS, increasing customer satisfaction by 20%.",
        "Created backend APIs in Express.js to handle user authentication and data processing.",
        "Wrote unit tests with Jest to ensure 90% code coverage.",
        "Assisted in deploying containerized applications using Docker."
      ]
    }
  ],
  "projects": [
    {
      "title": "Supply Chain Web Application",
      "description": [
        "Designed and built a full-stack application to manage product lifecycle and shipment tracking.",
        "Implemented role-based access and secure authentication using JWT."
      ],
      "tech_stack": "React.js, Node.js, PostgreSQL, TailwindCSS, Azure Container Apps"
    },
    {
      "title": "AI Resume Optimizer (Based on Job Description)",
      "description": [
        "Developed an AI-powered tool to tailor resumes using job descriptions with keyword optimization.",
        "Implemented PDF parsing and GPT integration for automated summary rewriting."
      ],
      "tech_stack": "Flask, React.js, OpenAI API, MongoDB"
    }
  ],
  "education": [
    {
      "institution": "National Institute of Technology, Calicut",
      "degree": "B.Tech in Computer Science and Engineering",
      "start_date": "2018",
      "end_date": "2022",
      "cgpa": "8.5",
      "percentage": "85%"
    }
  ],
  "certifications": [
    {
      "title": "Full Stack Web Development with React",
      "start_date": "2022-01",
      "end_date": "2022-06",
      "organization": "Coursera / Hong Kong University of Science and Technology"
    },
    {
      "title": "Azure Fundamentals (AZ-900)",
      "start_date": "2023-02",
      "end_date": "2023-03",
      "organization": "Microsoft"
    }
  ],
  "hobbies": ["Swimming", "Reading Tech Blogs", "Photography"],
  "languages": ["English", "Hindi", "Malayalam"]
}
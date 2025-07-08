from flask import Flask, jsonify, request
from functions.Helper_Functions import clean_json_output
import os
from functions.PDF_Functions import extract_text_from_pdf, generate_resume_from_html
from functions.AI_Functions import generate_enhanced_resume
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER") or r'uploadFolder'
UI_BASE_URL = os.getenv("UI_BASE_URL") or "http://localhost:3000"
app = Flask(__name__) 
CORS(app, origins=[UI_BASE_URL], supports_credentials=True)

@app.route("/upload", methods=[ "POST"])
def upload_resume():

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # CHECK IF THE REQUEST OBJECT HAS FILES AND JOB DESCRIPTION
    if 'resume' not in request.files or request.form.get('job') is None:
        return jsonify({"error": "No file part or job description provided"}), 400
        
    file = request.files['resume']
    if file.filename == '':
            return jsonify({"error": "No file selected"}), 400
        
    if file and file.filename.endswith('.pdf'):

        # SAVING THE FILE TO THE UPLOAD FOLDER
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        extracted_resume = extract_text_from_pdf(filepath)
        job_description = request.form.get('job')
        enhanced_resume = generate_enhanced_resume(job_description, extracted_resume)
        return clean_json_output(enhanced_resume), 200

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, jsonify, request, g
from functions.Helper_Functions import *
from functions.DatabaseFunctions import *
import os
from functions.PDF_Functions import extract_text_from_pdf, generate_resume_from_html
from functions.AI_Functions import generate_enhanced_resume
from dotenv import load_dotenv
from flask_cors import CORS
from models.user import User
from models.resume import Resume
from common.routes import PUBLIC_ROUTES
load_dotenv()

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER") or r'uploadFolder'
UI_BASE_URL = os.getenv("UI_BASE_URL") or "https://ai-resume-enhancer-frontend.vercel.app"
app = Flask(__name__) 
print(UI_BASE_URL)
CORS(app, origins=[UI_BASE_URL])



@app.before_request
def check_auth():
    if request.method == "OPTIONS":
        return '', 200  # Let CORS preflight pass
    url_path = request.path
    if(url_path not in PUBLIC_ROUTES):
        token = request.headers.get('Authorization')
        if(token is None):
            return error_response_formatter(data="Please Send Authorization Token", status=400)
        user = decode_jwt(jwt_token=token.replace("Bearer ", ""))
        if(user is False):
            return error_response_formatter(data="Token Invalid", status=400)
        else :
            g.user = user

@app.route("/upload", methods=[ "POST"])
def upload_resume():

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # CHECK IF THE REQUEST OBJECT HAS FILES AND JOB DESCRIPTION
    if 'resume' not in request.files or request.form.get('job') is None:
        return error_response_formatter("Please send the required fields", 400)
        
    file = request.files['resume']
    if file.filename == '':
            return error_response_formatter("Please send the required fields", 400)
        
    if file and file.filename.endswith('.pdf'):

        # SAVING THE FILE TO THE UPLOAD FOLDER
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)
        extracted_resume = extract_text_from_pdf(filepath)
        job_description = request.form.get('job')
        enhanced_resume = generate_enhanced_resume(job_description, extracted_resume)
        return clean_json_output(enhanced_resume), 200

        # return success_response_formatter(data=enhanced_resume)
        
@app.route("/hello", methods=["GET"])
def hello():
    return success_response_formatter("Hello, World!")

@app.route("/signup", methods=["POST"])
def signup():
     body = request.json
     if 'email' not in body or 'password' not in body or 'name' not in body:
        return error_response_formatter("Please send the required fields", 400)
     
     checkUser = getUser(body["email"])
     
     if checkUser:
         return error_response_formatter("User exists with the same email", 400)
     
     hash_pass = generate_password_hash(body["password"])

     user = User(body["email"], hash_pass, body["name"])

     createUser(user.getUser())

     return success_response_formatter(hash_pass)


@app.route("/login", methods=["POST"])
def login():
    body = request.json
    print(body)
    if 'email' not in body or 'password' not in body:
        print("First Error")
        return error_response_formatter("Please send the required fields", 400)
    checkUser = getUser(body["email"])
     
    if checkUser is None:
        print("Second Error")
        return error_response_formatter("Please Enter Correct Credentials", 400)
    
    print(checkUser[0])
    hash_pwd = checkUser[0]["password"]

    if(not compare_password_hash(body["password"], hash_pwd)):
        print("Third Error")
        return error_response_formatter("Please Enter Correct Credentials", 400)
    
    jwt_token = generate_jwt(checkUser[0])

    
    return success_response_formatter({
        "email" : checkUser[0]["email"],
        "name" : checkUser[0]["name"],
        "id" : str(checkUser[0]["_id"]),
        "accessToken" : jwt_token
    })
    

@app.route("/save", methods=["POST"])
def save_resume():
    body = request.json
    resume = Resume(
    body["name"],
    body["job_role"],
    body["mobile"],
    body["email"],
    body["linkedin"],
    body["github"],
    body["professional_summary"],
    body["key_skills"],
    body["experience"],
    body["projects"],
    body["education"],
    body["certifications"],
    body["hobbies"],
    body["languages"])

    save_resume(resume.get_resume())

    return success_response_formatter("Saved Successfully")



if __name__ == '__main__':
    app.run(debug=True)
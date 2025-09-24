import os
import pymongo
from dotenv import load_dotenv
import json

# Load environment variables from a .env file
load_dotenv()

# Get the MongoDB connection string from environment variables
CONNECTION_STRING = os.environ.get("MONGO_URI") or ""

# Create a MongoDB client using the connection string
client = pymongo.MongoClient(CONNECTION_STRING, serverSelectionTimeoutMS=5000)

# Access the 'resume_db' database
resume = client.resume_db

# Access the 'enhanced_resumes' collection within the 'resume_db' database
enhanced_resumes = resume.enhanced_resumes

# Access the 'users' collection within the 'resume_db' database
users = resume.users


from bson import ObjectId

def serialize_doc(doc):
    """Convert ObjectId fields to strings in a document."""
    if not doc:
        return doc
    doc = dict(doc)
    for key, value in doc.items():
        if isinstance(value, ObjectId):
            doc[key] = str(value)
    return doc

def getUser(email):
    user = list(users.find({"email" : email}))
    user = [serialize_doc(u) for u in user]
    if user:
        return user
    else:
        return None
    
def createUser(user):
    users.insert_one(user)
    return

def saveResume(resume):
    enhanced_resumes.insert_one(resume)
    return

def getResumes(user_id):
    resumes = list(enhanced_resumes.find({"user_id" : user_id}))
    resumes = [serialize_doc(r) for r in resumes]
    return resumes

def editResume(resume_id, resume):
    enhanced_resumes.update_one(
        {"_id": ObjectId(resume_id)},
        {"$set": resume}
    )
    return serialize_doc(enhanced_resumes.find_one({"_id": ObjectId(resume_id)}))

def deleteResume(resume_id):
    enhanced_resumes.delete_one({"_id": ObjectId(resume_id)})
    return




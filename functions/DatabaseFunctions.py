import os
import pymongo
from dotenv import load_dotenv
import json

# Load environment variables from a .env file
load_dotenv()

# Get the MongoDB connection string from environment variables
CONNECTION_STRING = os.environ.get("CONNECTION_STRING") or "mongodb+srv://resumesuperuser:XbJ11L4FBhGDFuN@ai-backend-mongo-cluster.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"

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




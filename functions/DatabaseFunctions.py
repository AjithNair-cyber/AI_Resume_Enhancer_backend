import os
import pymongo
from dotenv import load_dotenv
import json

# Load environment variables from a .env file
load_dotenv()

# Get the MongoDB connection string from environment variables
CONNECTION_STRING = os.environ.get("CONNECTION_STRING") | "mongodb+srv://resumesuperuser:XbJ11L4FBhGDFuN@ai-backend-mongo-cluster.global.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"

# Create a MongoDB client using the connection string
client = pymongo.MongoClient(CONNECTION_STRING)

# Access the 'resume_db' database
resume = client.resume_db

# Access the 'enhanced_resumes' collection within the 'resume_db' database
enhanced_resumes = resume.enhanced_resumes

# Access the 'users' collection within the 'resume_db' database
users = resume.users


def getUser(email):
    user = list(users.find({"email" : email}))
    # print(user)
    if user:
        return user
    else:
        return None
    
def createUser(user):
    users.insert_one(user)
    return

def save_resume(resume):
    enhanced_resumes.insert(resume)
    return




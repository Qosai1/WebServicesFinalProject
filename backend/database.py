from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")


db = client["human_rights_db"]


incident_reports = db["incident_reports"]
cases_collection = db["cases"]  
users_collection = db["users"]
victims_collection = db["victims"]
risk_collection = db["victim_risk_assessments"]
case_status_history_collection = db["case_status_history"]
report_evidence_collection = db["report_evidence"]



# email = "Qusai@gmail.com"
# password = "Qusai123"
# role = "admin"

# users_collection.delete_one({"email": email}) 

# hashed_pw = hash_password(password)

# users_collection.insert_one({
#     "email": email,
#     "password": hashed_pw,
#     "role": role
# })

# print("Admin added with bcrypt password.")





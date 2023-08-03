import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("adsproj-f1323-firebase-adminsdk-2ejx9-7eeee89a2f.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
    
# collection_ref = db.collection('users')

# with open('./templates/added_meal.json') as file:
#     existing_meals = json.load(file)
# # docs = collection_ref.get()


# db.collection("users").document("mitulkrishna2003@gmail.com").update({'added_meals' :existing_meals})


def post_added_meals(data) :
    db.collection("users").document("mitulkrishna2003@gmail.com").update({'added_meals' :data})

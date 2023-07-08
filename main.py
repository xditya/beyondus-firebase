# write data from csv to firestore

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from read_csv import readcsv

# Path to the service account key JSON file
cred = credentials.Certificate('serviceAccountKey.json')

# Initialize the app with the service account key
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Create a reference to the hospitals collection
hospitals_ref = db.collection('hospital_data')

for hospital in readcsv():
    hospitals_ref.document(hospital["name"]).set(hospital)
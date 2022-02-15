import os   

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def get_reference():
    cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIAL'))
    firebase_admin.initialize_app(cred, {'databaseURL':os.getenv('DATABASE_URL')})

    ref = db.reference("/books")

    return ref
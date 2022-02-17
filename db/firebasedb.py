import os
from ast import literal_eval

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def get_reference():
    cred = credentials.Certificate(literal_eval(os.getenv('FIREBASE_CREDENTIAL')))
    firebase_admin.initialize_app(cred, {'databaseURL':os.getenv('DATABASE_URL')})

    ref = db.reference("/books")

    return ref
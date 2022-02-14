import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("../config/llr-library-backend-firebase-adminsdk-tcufi-e521d073ce.json")
firebase_admin.initialize_app(cred, {'databaseURL':'https://llr-library-backend-default-rtdb.firebaseio.com/'})

ref = db.reference("/books")

book = {
    'title':'temp',
    'body':'temp'
}


def add_book(book):
    key = ref.push(book).key
    # print(key)
    if(key):
        ref.child(key).child("id").set(key)
    return key

def get_book(id):
    book = ref.child(id).get()
    return book

def get_all():
    books = ref.get()
    return books

def update_book(id, arg,val):
    ref.child(id).child(arg).set(val)
    book = ref.child(id).get()
    return book

def delete_book(id):
    ref.child(id).delete()



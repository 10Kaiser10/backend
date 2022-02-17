from db.firebasedb import get_reference

ref = get_reference()

def add_book(book):
    key = ref.push(book).key
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
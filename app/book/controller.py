from app.book.models import get_all


def api_post_data():
    return "Book Added", 200

def api_book_data():
    return "Book Data", 200

def api_allbook_data():
    return get_all(), 200


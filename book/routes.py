from flask import Blueprint
from controller import *

books_api = Blueprint('books', __name__)

books_api.add_url_rule(
    rule="/books/add", view_func=api_post_data, methods=["POST"])


books_api.add_url_rule(
    rule="/books/get/<book_id>", view_func=api_book_data, methods=["GET"])


books_api.add_url_rule(
    rule="/books/get_all", view_func=api_allbook_data, methods=["GET"])




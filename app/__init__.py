import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

from app.home.routes import home_api
from app.book.routes import books_api

app.register_blueprint(home_api)
app.register_blueprint(books_api)
# import sqlite3
from flask import Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)

class User(db.Model):
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Float, primary_key=True)

    def __repr__(self):
        return f"User('{self.title}', '{self.author}', '{self.rating}')"


from marshmallow import Schema, fields

from setup_db import db


class Book(db.Model):
    __tablename__ = 'books'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    year = db.Column(db.Integer)
    pages = db.Column(db.Integer)


class BooksSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    author = fields.Str()
    year = fields.Int()
    pages = fields.Int()


class Review(db.Model):
    __tablename__ = 'reviews'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    book_id = db.Column(db.Integer)


class ReviewsSchema(Schema):
    id = fields.Int()
    user = fields.Str()
    rating = fields.Int()
    book_id = fields.Int()


from flask import request
from flask_restx import Namespace, Resource

from part1.final.models import Book, BooksSchema
from part1.final.setup_db import db

book_ns = Namespace('books')

book_schema = BooksSchema()
books_schema = BooksSchema(many=True)


@book_ns.route('/')
class BooksView(Resource):
    def get(self):
        all_books = db.session.query(Book).all()

        return books_schema.dump(all_books), 200

    def post(self):
        req_json = request.json
        new_book = Book(**req_json)

        with db.session.begin():
            db.session.add(new_book)

            return "", 201


@book_ns.route('/<int:bid>')
class BookView(Resource):
    def get(self, bid: int):
        try:
            book = db.session.query(Book).filter(Book.id == bid).one()
            return book_schema.dump(book), 200
        except Exception as e:
            return str(e), 404

    def put(self, bid: int):
        book = db.session.query(Book).get(bid)
        req_json = request.json

        book.name = req_json.get("name")
        book.author = req_json.get("author")
        book.year = req_json.get("year")
        book.pages = req_json.get("pages")

        db.session.add(book)
        db.session.commit()

        return "", 204

    def delete(self, bid: int):
        book = db.session.query(Book).get(bid)

        db.session.delete(book)
        db.session.commit()

        return "", 204


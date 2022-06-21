from flask import request
from flask_restx import Namespace, Resource

from part1.final.models import Review, ReviewsSchema
from part1.final.setup_db import db

review_ns = Namespace('reviews')

review_schema = ReviewsSchema()
reviews_schema = ReviewsSchema(many=True)


@review_ns.route('/')
class ReviewsView(Resource):
    def get(self):
        all_reviews = db.session.query(Review).all()

        return reviews_schema.dump(all_reviews), 200

    def post(self):
        req_json = request.json
        new_review = Review(**req_json)

        with db.session.begin():
            db.session.add(new_review)

            return "", 201


@review_ns.route('/<int:rid>')
class ReviewView(Resource):
    def get(self, rid: int):
        try:
            review = db.session.query(Review).filter(Review.id == rid).one()
            return review_schema.dump(review), 200
        except Exception as e:
            return str(e), 404

    def put(self, rid: int):
        review = db.session.query(Review).get(rid)
        req_json = request.json

        review.user = req_json.get("user")
        review.rating = req_json.get("rating")
        review.book_id = req_json.get("book_id")

        db.session.add(review)
        db.session.commit()

        return "", 204

    def delete(self, rid: int):
        review = db.session.query(Review).get(rid)

        db.session.delete(review)
        db.session.commit()

        return "", 204

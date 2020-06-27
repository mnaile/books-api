from flask import Flask, request,jsonify
from app.model import Books
from app.serializer import BookSchema, UpdateBookSchema
from app_init.app_factory import create_app
from marshmallow import ValidationError
from http import HTTPStatus
import requests

app = create_app()

# create book

@app.route('/books', methods=["POST"])
def create():
    book_info = request.get_json()
    try:
        book = BookSchema().load(book_info)
        
        
        book.save_db()
        
    except ValidationError as err:
        return jsonify(err.messages),HTTPStatus.BAD_REQUEST

    return BookSchema().jsonify(book),HTTPStatus.OK


# read book

@app.route('/books/<int:id>', methods=["GET"])
def get_book(id):
    book_info = Books.query.filter_by(id=id).first()
   

    if book_info :
        # schema = BookSchema()
        # book_info = schema.dump(book_info)
        # book_info["user_id"] = response.json()
        return BookSchema().jsonify(book_info),HTTPStatus.OK
    return jsonify(msg="Book not found!"),HTTPStatus.NOT_FOUND

@app.route('/books', methods=["GET"])
def get_all_book():
    book_info = Books.query.all()
    
    

    return BookSchema().jsonify(book_info, many=True),HTTPStatus.OK


# delete book

@app.route('/books/<int:id>', methods=["DELETE"])
def delete_book(id):
    book_info = Books.query.filter_by(id=id).first()
    if book_info:
        book_info.delete_from_db()
        return jsonify(msg="Book deleted!"),HTTPStatus.OK
    return jsonify(msg="Book not found!")

# update book

@app.route('/books/<int:id>', methods=["PUT"])
def update_book(id):
    book_info = Books.query.filter_by(id=id).first()
    if book_info:
        book = request.get_json()

        book = UpdateBookSchema().load(book)

        book_info.update_db(**book)
        
        
        return BookSchema().jsonify(book),HTTPStatus.OK
    return jsonify(msg="Book not found!"),HTTPStatus.NOT_FOUND


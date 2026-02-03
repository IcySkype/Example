from flask import Blueprint, jsonify, request

books_bp = Blueprint('books_bp', __name__)

# Mock Database
books = [
    {"id": 1, 
"title": "The Hobbit", 
"author": "J.R.R. Tolkien"},
    {"id": 2, 
"title": "1984", 
"author": "George Orwell"},
    {"id":3, 
     "title": "Harry Potter", 
     "author" : "JK Rowling"
    }
]

@books_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@books_bp.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(new_book), 201

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Not found"}), 404
    data = request.get_json()
    book.update(data)
    return jsonify(book)

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b["id"] != book_id]
    return jsonify({"message": "Deleted"}), 200

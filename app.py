from flask import Flask, jsonify
from flask_cors import CORS
from books_bp import books_bp

app = Flask(__name__)
CORS(app)

# Register Blueprint with a URL Prefix
app.register_blueprint(books_bp, url_prefix='/api/v1')

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

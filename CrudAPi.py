from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), unique=False, nullable=False)
    author = db.Column(db.String(40), unique=False, nullable=False)
    publisher = db.Column(db.String(40), unique=False, nullable=False)

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(book_name=data['book_name'], author=data['author'], publisher=data['publisher'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(data["author"]), 201

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        book_list.append(book_data)
    return jsonify({'books': book_list})

# Read a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        book_data = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        return jsonify(book_data)
    else:
        return jsonify({'message': 'Book not found'}), 404
    
@app.route('/update/<int:book_id>', methods= ['POST'])
def update_book(book_id):
    data = request.get_json()
    book = Book.query.get(book_id)
    book.author = data['author']
    book.book_name = data['book_name']
    book.publisher = data['publisher']
    db.session.commit()
    return jsonify('record updated!')
    
@app.route('/delete/<int:book_id>', methods= ['POST'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify('record deleted!')  
    
@app.route('/', methods=['GET'])
def get_home():
    return jsonify({'Book Data2': ' Books'})


with app.app_context():
    db.create_all()
if __name__ == '__main__':
    app.run(debug=True, port=8000)

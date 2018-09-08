from app import app
from flask import jsonify
from flask import request

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
              <p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/v1/resources/books/all',methods=['GET'])
def get_all():
    return jsonify(books)
# Loop through the data and match results that fit the requested ID.
# IDs are unique, but other fields might return many results
@app.route('/api/v1/resources/books/<string:id>',methods=['GET'])
def api_id(id):
    if id:
        book_id = int(id)
    else:
        return "Error: No id field provided. Please specify an id."
    # Create an empty list for our results
    results = []
    for book in books:
        if book['id'] == book_id:
            results.append(book)
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
#updating a list
@app.route('/api/v1/resources/books/update/<string:id>',methods=['PUT'])
def update_book(id):
    if(request.method == 'PUT'):
        if id:
            book_id = int(id)
        else:
            return "Error: No id field provided. Please specify an id."
        for book in books:
            if book['id'] == book_id:
                some_json = request.get_json()
                book['id']= book_id
                book['title'] = some_json['title']
                book['author'] = some_json['author']
                book['first_sentence']=some_json['first_sentence']
                book['published'] = some_json['published']
        return jsonify(books)


#Adding a book to the list
@app.route('/api/v1/resources/books/add',methods=['POST'])
def add_book():
    if (request.method == 'POST'):
        some_json = request.get_json()
        books.append(some_json)
        return jsonify(books)
# Deleting a book
@app.route('/api/v1/resources/books/delete/<string:id>',methods=['DELETE'])
def delete_book(id):
    if (request.method == 'DELETE'):
        if id:
            book_id = int(id)
        else:
            return "Error: No id field provided. Please specify an id."
        for book in books:
            if book['id'] == book_id:
                books.remove(book)
        return jsonify(books)
    

    




        




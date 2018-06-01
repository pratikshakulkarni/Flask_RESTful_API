from flask import Flask,jsonify,request

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring', 
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/',methods=['GET'])
def home():
	return "<h1> This will be printed!</h1>"

@app.route('/books',methods=['GET'])
def ret_all():
	return jsonify(books)
@app.route('/resources',methods=['GET'])
def  res():
	if 'id' in request.args:
		id = int(request.args['id'])
	else:
		return "No id provided!"
	result = []

	for book in books:
		if book['id'] == id:
			result.append(book)
	return jsonify(result)

app.run(debug=True,port=8080)

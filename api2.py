from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {'name': 'blacky',
     'pass':'123'},
     {'name': 'boki',
     'pass':'12345'}
]

@app.route('/',methods=['GET'])
def home():
	return "<h1> API Authentication</h1>"

@app.route('/valid',methods=['GET'])
def valid():
    if 'name' in request.args:
        name = request.args['name']
        if 'pass' in request.args:
            pass1 = request.args['pass']
        else:
            return "pass not provided"
        
    else:
        return "No name provided!"

   
    flag = 0
    for name1 in data:
        see = (name1['name'] == name) and (name1['pass'] == pass1)

        if(see):
            flag = 1
            break;
        else:
            continue
    if flag == 1:
        return "Authenticated!"
    else:
        return "not Authenticated!"



app.run(debug=True,port=5001)

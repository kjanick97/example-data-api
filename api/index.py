from flask import Flask, Response
import requests
import json


app = Flask(__name__)


# simple hello message on default path to check if app is running
@app.route('/', methods = ['GET'])
def sayHello():
    return "Hello I am up and running"
        
        
@app.route('/getPlayerData', methods = ['GET'])
def getData():
    
    footballplayers = [
        ("defender", 89, 35, False, "Sergio Ramos", "Male"),
        ("midfielder", 84, 25, False, "Dele", "Male"),
        ("defender", 84, 29, False, "Joel Matip", "Male"),
        ("striker", 89, 27, True, "Harry Kane", "Male"),
        ("striker", 93, 33, True, "Lionel Messi", "Male"),
        ("goalkeeper", 88, 27, False, "Ederson", "Male"),
        (None, 78, 29, False, "Fabian Schär", "Male"), # defender
        ("midfielder", 91, 29, False, "Kevin De Bruyne", "Male"),
        (None, 90, 32, True, "Sergio Agüero", "Male"),  # striker
        ("goalkeeper", 91, 28, False, "Jan Oblak", "Male"),
        ("striker", 93, 35, False, "Megan Rapinoe", "Female"),
        ("striker", 90, 31, False, "Alex Morgan", "Female"),
        ("defender", 92, 30, False, "Wendie Renard", "Female")
    ]
    
    json_data = json.dumps(footballplayers)
        
    # create response
    resp = Response(json_data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    
    return resp


from flask import Flask
from flask import render_template,jsonify,request
import requests
import random

#this is for cross origin
from flask_cors import CORS


#for rasa agent
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter



#for JSON
import json
from pprint import pprint

app=Flask(__name__)

#giving cross origin access
CORS(app)



@app.route('/')
def index():
    print("Here at least")
    return render_template('home.html')    

def format_entities(entities):
    """
    formats entities to key value pairs
    """
    ## Should be formatted to handle multiple entity values
    # e = {"day":None,"time":None,"place":None}
    e = {}
    for entity in entities:
        e[entity["entity"]] = entity["value"]
    return e




def getResult(msg):
    #here make call to the function interpreter



    url = 'http://localhost:5005/webhooks/rest/webhook'
    payload = { "sender": "das", "message": msg}
    headers = {'content-type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print("response type is ",type(response))
    print("raw text is ",response.json()[0])
    return response.json()[0]




@app.route('/chat',methods=["POST"])
def chat():
    
    try:
        print("Sending "+ request.form["text"]+"  to  getresult")
        response=getResult(request.form["text"])
        print("response from agent is "+str(response))
        response_text=response["text"]
        print("extracted the text")
        return jsonify({"status":"success","response":response_text})
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})



if __name__ == '__main__':
    print("#main")
    app.debug=True
    app.run(host='0.0.0.0', port=5090)
    
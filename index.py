from flask import Flask, request, jsonify
import os
import dialogflow
import requests
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print(request)
    print(request.json)
    print("client:" + request.json["queryResult"]["queryText"])
    print("server:" + request.json["queryResult"]["fulfillmentText"])
    return "1"

# run Flask app
if __name__ == "__main__":
    app.run("127.0.0.1",port=5002)
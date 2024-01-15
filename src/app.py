from flask import *
import requests
import json 
from dotenv import load_dotenv
import os


app = Flask(__name__)

url = "api.url"
response = requests.get(url)
response_json = response.json()

def loadenv(): 
    load_dotenv()
    API_TOKEN = os.getenv('API_TOKEN')


@app.route('/')
def home():
    loadenv()
    return response_json


app.run(debug=True)


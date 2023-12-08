from flask import *
import requests
import json 
from init import *


app = Flask(__name__)

@app.route('/')
def home():
    init()
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)


from crypt import methods
from flask import Flask,render_template,request
import requests

from data import datafake

import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/numpydata')
def renderTemplate():
    return showIndex()

@app.route('/query-example', methods=['POST'])
def query_example():
    # handle the POST request
    if request.method == 'POST':
        a = request.form.get('language')
        b = request.form.get('framework')       
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(a, b)

@app.route('/requests', methods=['GET'])
def getData():
    response = requests.get('https://api.github.com')
    #print(response.status_code)
    #response.status_code = 404
    if response.status_code == 200:
        return 'Request Succesfull'
    elif response.status_code == 404:
        return 'Resource not found'
    elif response.status_code == 500:
        return 'Request Failed'    
        
        
        

def showIndex():
    data:list = datafake.returnAges()    
    #newdata = np.array_split(data,10)
    return str(data)
    #return render_template('index.html', data=data)
import flask
from flask import *
app = Flask( _name_, static_url_path='/static') 

@app.route('/')
def Home():
    return render_template('index.html')

@app.route("")
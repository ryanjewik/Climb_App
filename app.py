from flask import Flask
from sqlalchemy import create_engine
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask"
from flask import Flask, render_template, redirect, url_for,session
from flask import request
from sqlalchemy import create_engine
app = Flask(__name__)
app.secret_key = 'super secret key'

'''

HOME PAGE.  WE CAN DO SOMETHING HERE AT SOME POINT, AND ROUTING FUNCTIONALITY.  MAYBE SOMETHING LIKE COMMUNITY NEWS

'''
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


'''

USER PROFILE PAGE.  ADD FUNCTIONALITY TO SEE THINGS LISTED ON THE USERS PROFILE, SUCH AS NAME, COMPLETED CLIMBS, ETC.

'''
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


'''

LOGIN PAGE.  NEED TO IMPLEMENT DATABASE FUNCTIONALITY TO CHECK IF USERNAME/PASSWORD COMBO IS IN DATABASE

'''

@app.route('/login',methods = ['GET','POST'])
def login():
    error = None
    if(request.method == 'POST'):
        if request.form['username'] != 'root' or request.form['password'] != 'admin':
            error = 'Invalid Account Credentials, Try Again'
        else:
            session['username'] = "Root User"
            return render_template('hello.html', name=session['username'])
    return render_template('login.html',error=error)  


'''

CLIMB PAGE.  WILL LOOK THROUGH CLIMB DATABSE TO SEE IF CLIMB NAME IS PRESENT.  IF IT IS, RETURN NECESSARY INFORMATION

'''
@app.route('/climb/')
@app.route('/climb/<climbName>')
def climbpage(climbName = None,climbDifficulty = None,climbType = None,climbSpot = None):

    if(climbName == "Stem Gem"):
        climbDifficulty = "V4"
        climbType = "Boulder"
        climbSpot = "Joshua Tree"

        error  = None
    else:
        error = "Climb " + str(climbName) + " not Found"

    return render_template('climb.html',climbName = climbName,climbDifficulty = climbDifficulty,climbType = climbType,climbSpot = climbSpot, error=error)
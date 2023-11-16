from flask import Flask, render_template, redirect, url_for,session
from flask import request
from sqlalchemy import create_engine
app = Flask(__name__)
app.secret_key = 'super secret key'



class Climb:
    def __init__(self,climbName,climbDifficulty,climbType,climbSpot):
        self.climbName = climbName
        self.climbDifficulty = climbDifficulty
        self.climbType = climbType
        self.climbSpot = climbSpot


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
def climbpage(climbName = None,climb = None):
    climbArr = []

    # CREATE LIST OF DESIRED CLIMBS FROM DATABASE, EITHER USER OR AREA OR STATE
    for i in range(100):
        climbArr.append(Climb("Climb " + str(i),str(i),str(i),str(i)))

    if(climbArr):
        error = None
    else:
        
        error = "Climbs not Found"
    
    return render_template('climb.html',error=error, climbArr = climbArr)

@app.route('/climb/<climbName>')
def singleClimb(climbName = None):
        error = None
        climb = Climb(climbName,"V4","Boulder","Joshua Tree")
        return render_template('singleClimb.html',climb = climb, error=error)

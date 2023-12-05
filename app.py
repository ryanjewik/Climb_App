from flask import Flask, render_template, redirect, url_for,session
from flask import request
import random
from sqlalchemy import create_engine
from sqlalchemy import text
import random


connection_string = "mysql+mysqlconnector://root:CPSC408!@localhost:3306/climbing_db"
engine = create_engine(connection_string, echo=True)

app = Flask(__name__)

climbExample = (1, 'Wet Hug', 0, 'Boulder', 1)

app.secret_key = 'super secret keys'
conn = engine.connect()


'''

ADD DATABASE CONNECTION

'''

class Climb:
    def __init__(self,climbTuple):
        self.climbName = climbTuple[1]
        self.climbDifficulty = climbTuple[2]
        self.climbType = climbTuple[3]

        
        query = text("SELECT * FROM climbingspots WHERE spotID = :spot_id")

# Execute the query with the bind parameter
        res = conn.execute(query, {"spot_id": climbTuple[4]}).fetchall()

        self.climbSpot = res[0][1]





       # self.climbSpot = climbSpot


'''

HOME PAGE.  WE CAN DO SOMETHING HERE AT SOME POINT, AND ROUTING FUNCTIONALITY.  MAYBE SOMETHING LIKE COMMUNITY NEWS
JACCOB MAU

TODO SHOWS TOP X CLIMBS 
TODO POTENTIALLY WITH IMAGES

'''
@app.route("/")
@app.route("/home")
def home():
    # Query to fetch top 5 climbs
    query = text("SELECT ClimbName, Rating FROM climbs ORDER BY Rating DESC LIMIT 5")
    top_climbs = conn.execute(query).fetchall()

    # Convert to list of dictionaries
    climbs_list = [{"name": climb[0], "rating": climb[1]} for climb in top_climbs]

    return render_template('home.html', top_climbs=climbs_list)

'''
SZYMON KOZLOWSKI

TODO TAB OF USER PROFILE.

TODO FEATURES LIKE COMPLETED CLIMBS, MARKING CLIMBS YOU'VE DONE


'''
@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)



'''

LOGIN PAGE.  NEED TO IMPLEMENT DATABASE FUNCTIONALITY TO CHECK IF USERNAME/PASSWORD COMBO IS IN DATABASE

SZYMON KOZLOWSKI

TODO ROUTE TO USER PROFILE

TODO CHECK DATABASE FOR USER


'''
@app.route('/leaderboard')

def leaderboard():
    userArr = []
    query = text("SELECT COUNT(users.UserID),users.Username FROM users JOIN completedclimbs ON users.UserID = completedclimbs.UserID GROUP BY users.UserID ORDER BY COUNT(users.UserID) DESC LIMIT 10")
    res = conn.execute(query).fetchall()
    # print(res)

    for i in range(len(res)):
        userArr.append((res[i][1],res[i][0]))
    print(userArr)
    return render_template('leaderboard.html',userArr = userArr,len = len(userArr))


@app.route('/user/')
@app.route('/user/<name>')

def user(name=None,methods = ['GET','POST']):
    if('userID' in session):
        name = session['username']
        climbArr = []    
        ratingSpots = []
        query = text("SELECT climbs.*,climbingspots.SpotName,completedclimbs.Rating FROM climbs JOIN completedclimbs ON climbs.climbID = completedclimbs.climbID JOIN climbingspots ON climbingspots.SpotID = climbs.SpotID WHERE completedclimbs.userID = :userID")
        res = conn.execute(query, {"userID": session['userID']}).fetchall()
        print(res)

        for i in range(len(res)):
            climbArr.append(Climb(res[i]))
            ratingSpots.append((res[i][5],res[i][6]))
        print(ratingSpots)
        return render_template('hello.html', name=name,climbArr = climbArr,len=len(climbArr),ratingSpots = ratingSpots)
    else:
        return redirect(url_for('login'))
        

@app.route('/login',methods = ['GET','POST'])
def login():
    session.clear()
    error = None

    if(request.method == 'POST'):
        query = text("SELECT Password,UserID FROM users WHERE Username = :username")

# Execute the query with the bind parameter
        print(request.form['username'])
        res = conn.execute(query, {"username": request.form['username']}).fetchone()
        print(res)
        #if request.form['username'] != 'root' or request.form['password'] != 'admin':
        if res and request.form['password'] == res[0]:
            session['username'] = request.form['username']
            session['userID'] = res[1]
            # return render_template('hello.html', name=session['username'])
            return redirect(url_for('user', name=session['username']))
            
        else:
            error = 'Invalid Account Credentials, Try Again'

    return render_template('login.html',error=error)  

@app.route('/register',methods = ['GET','POST'])
def register():
    error = None
    user = ""
    if(request.method == 'POST'):
        print(request.form['usernameRegister'])
        print(request.form['passwordRegister'])
        query = text("INSERT INTO users (Username, Password) VALUES (:username, :password)")

        try:
            user = request.form['usernameRegister'] 
            conn.execute(query, {"username":user,"password": request.form['passwordRegister']})
            conn.commit()
            
            '''
            query = text("SELECT Password,UserID FROM users WHERE Username = :username")
            res = conn.execute(query, {"username": request.form['username']}).fetchone()
            print(res)
            print(session['userID'])
            session['userID'] = res[1]
            '''
            
            
        except:
            print("augh")
            error = 'Username is taken'
            

        if(error == None):
            session['username'] = request.form['usernameRegister']

            print("UAHFHEWFIUHIHUFEWUIHFWEIUHFIUH")
            
            query = text("SELECT Password,UserID FROM users WHERE Username = :username")
            res = conn.execute(query, {"username": user}).fetchone()
            
            session['userID'] = res[1]

            return redirect(url_for('user', name=session['username']))

    return render_template('register.html',error=error)  

'''

CLIMB PAGE.  WILL LOOK THROUGH CLIMB DATABSE TO SEE IF CLIMB NAME IS PRESENT.  IF IT IS, RETURN NECESSARY INFORMATION

RYAN JEWIK

TODO DISPLAY STATES -> LOCATIONS -> SPOTS -> SHOW ALL CLIMBS FOR SAID SPOT X

TODO POTENTIALLY RANDOM CLIMB FEATURE OR A SEARCH FUNCTION THAT POPULATES AN ARRAY WITH PARAMETERS

TODO RECOMMENDED CLIMB TAB.  IF USER IS LOGGED IN AND HAS COMPLETED CLIMBS, GENERATE TAILORED RECOMENDATIONS

'''
@app.route('/allClimbs/')
def allClimbs():
    query = "SELECT * FROM climbs"
    res = conn.execute(text(query)).fetchall()
    allClimbsArr = []
    for x in res:
        allClimbsArr.append(x[1])
    return render_template('allClimbs.html', climbArr= allClimbsArr)
    



@app.route('/random/')
def randomGen():
    query = "SELECT * FROM climbs"
    rand = conn.execute(text(query)).fetchall()
    
    index = random.randint(0,len(rand)-1)
    climb = Climb(rand[index])

    print(climb.climbName)
    print(climb.climbDifficulty)
    print(climb.climbSpot)
    print(climb.climbType)
    error = None
    return render_template('singleClimb.html',climb = climb, error=error)


@app.route('/recommendation/')
@app.route('/recommendation/<userName>/')
def recommendation(userName = None):
    if('username' in session):
        userName = session['username']
        query = "SELECT UserID, SkillLevel FROM users WHERE Username = '" + userName +"'"
        skillID = conn.execute(text(query)).fetchone()
        #holds the userID and skill level

        #want to grab every climb the user has not completed
        query = "SELECT ClimbID FROM completedclimbs WHERE UserID = '" + str(skillID[0])+"'"
        res = conn.execute(text(query)).fetchall()
        userClimbs = []
        for x in res:
            userClimbs.append(x[0])

        query = "SELECT ClimbID FROM climbs"
        res2 = conn.execute(text(query)).fetchall()
        notClimbed=[]
        for x in res2:
            if (x[0] not in userClimbs):
                notClimbed.append(x[0])
        if (len(notClimbed)==0): #if they have completed all climbs then just randomly select a climb
            print("all climbs completed")
            query = "SELECT * FROM climbs"
            rand = conn.execute(text(query)).fetchall()
            
            index = random.randint(0,len(userClimbs)-1)
            climb = Climb(rand[index])

            print(climb.climbName)
            print(climb.climbDifficulty)
            print(climb.climbSpot)
            print(climb.climbType)
        else:#recommends if there are climbs the user hasn't completed

            skill = int(skillID[1]) # will choose a range of climbs based on the self-proclaimed skill level
            if (skill == 1):
                lowerBound = 0
                upperBound = 3
            elif (skill == 2):
                lowerBound = 2
                upperBound = 5
            elif (skill == 3):
                lowerBound = 4
                upperBound = 7
            elif (skill == 4):
                lowerBound = 6
                upperBound = 9
            else:
                lowerBound = 10
                upperBound = 17
            query = "SELECT * FROM climbs WHERE Difficulty BETWEEN "+ str(lowerBound) + " AND " + str(upperBound)
            climbsInRange = conn.execute(text(query)).fetchall()
            while (len(climbsInRange) == 0): #if there are no climbs they haven't completed in that range it will stretch the bounds until it finds climbs
                lowerBound = lowerBound - 1
                upperBound = upperBound + 1
                query = "SELECT ClimbID FROM climbs WHERE Difficulty BETWEEN "+ str(lowerBound) + " AND " + str(upperBound)
                climbsInRange = conn.execute(text(query)).fetchall()
            climbsOptions = []
            for x in climbsInRange:
                if (x[0] in notClimbed):
                    climbsOptions.append(x[0])


            index = random.randint(0,len(climbsOptions)-1)#randomly choose a climb within the list
            climbID = climbsOptions[index]

            query = "SELECT * FROM climbs WHERE ClimbID = " + str(climbID)
            rec = conn.execute(text(query)).fetchall()
            climb = Climb(rec[0])

            print(climb.climbName)
            print(climb.climbDifficulty)
            print(climb.climbSpot)
            print(climb.climbType)
            
        

        #from that list depending on their skill level create a subset of that list
        #randomly choose one from that list and link it to it's singleClimb page



        error = None
        return render_template('singleClimb.html',climb = climb, error=error)
    else:
        return redirect(url_for('login'))
    


@app.route('/climb/')
@app.route('/<userName>/climb/')
def climbpage(climbName = None,climb = None,userName = None):
    climbArr = []
    '''
        if('username' in session):
        userName = session['username']
    '''

    # CREATE LIST OF DESIRED CLIMBS FROM DATABASE, EITHER USER OR AREA OR STATE

    res = conn.execute(text("SELECT * FROM climbs")).fetchall()
    error = None
    for x in res:
        climbArr.append(Climb(x))
    query = "SELECT State FROM Locations"
    
    states = conn.execute(text(query)).fetchall()
    statesArr = []
    for x in states:
        if x[0] not in statesArr:
            statesArr.append(x[0])
    
    if(climbArr):
        error = None
    else:
        
        error = "Climbs not Found"
    return render_template('states.html',error=error, statesArr = statesArr,userName = userName)

    #return render_template('climb.html',error=error, climbArr = climbArr,userName = userName)


@app.route('/climb/<stateName>')
def locations(stateName = None):
    query = "SELECT * FROM Locations WHERE State = '" + stateName+"'"
    res = conn.execute(text(query)).fetchall()
    locationsArr = []
    for x in res:
        locationsArr.append(x[2])
    error = None
    return render_template('locations.html',error=error, locationsArr = locationsArr,stateName = stateName)

@app.route('/climb/<stateName>/<locationName>')
def areas(locationName = None, stateName = None):
    query = "SELECT LocationID FROM locations WHERE City = '" + locationName +"'"
    locationID = conn.execute(text(query)).fetchone()
    query = "SELECT * FROM climbingareas WHERE LocationID = '" + str(locationID[0])+"'"
    res = conn.execute(text(query)).fetchall()
    areasArr = []
    for x in res:
        areasArr.append(x[1])
    error = None
    return render_template('areas.html',error=error, areasArr = areasArr,locationName = locationName, stateName = stateName)

@app.route('/climb/<stateName>/<locationName>/<areaName>')
def spots(locationName = None, stateName = None,areaName = None):
    query = "SELECT AreaID FROM climbingareas WHERE AreaName = '" + areaName +"'"
    areaID = conn.execute(text(query)).fetchone()
    query = "SELECT * FROM climbingspots WHERE AreaID = '" + str(areaID[0])+"'"
    res = conn.execute(text(query)).fetchall()
    spotsArr = []
    for x in res:
        spotsArr.append(x[1])
    error = None
    return render_template('spots.html',error=error, spotsArr = spotsArr,locationName = locationName, stateName = stateName, areaName = areaName)


@app.route('/climb/<stateName>/<locationName>/<areaName>/<spotName>')
def climb(locationName = None, stateName = None,areaName = None,spotName = None):
    query = "SELECT SpotID FROM climbingspots WHERE SpotName = '" + spotName +"'"
    SpotID = conn.execute(text(query)).fetchone()
    query = "SELECT ClimbName FROM climbs WHERE SpotID = '" + str(SpotID[0])+"'"
    res = conn.execute(text(query)).fetchall()
    climbArr = []
    for x in res:
        climbArr.append(x[0])
    error = None
    
    

    return render_template('climb.html',error=error, climbArr = climbArr,locationName = locationName, stateName = stateName, areaName = areaName, spotName = spotName)


'''

JACCOB MAU

TODO ADD RATING FEATURE IF USER IS LOGGED IN, AND HAS NOT RATED CLIMB

TODO POTENTIALLY ADD IMAGE

'''




@app.route('/climb/////<climbName>')
@app.route('/climb/<stateName>/<locationName>/<areaName>/<spotName>/<climbName>')
def singleClimb(climbName = None, stateName = None, locationName = None, areaName = None, spotName = None):
        query = "SELECT * FROM climbs WHERE ClimbName = '" + climbName+"'"
        res = conn.execute(text(query)).fetchall()

        '''
        
        SELECT CLIMBS WHERE USER = RYAN

        res = [(climb1),(climbs2)]

        for i in res:
            climbArr.append(Climb(res[i]))

        
        '''
        error = None
        climb = Climb(res[0])

        print(climb.climbName)
        print(climb.climbDifficulty)
        print(climb.climbSpot)
        print(climb.climbType)

        
        return render_template('singleClimb.html',climb = climb, error=error)


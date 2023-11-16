from flask import Flask, render_template, redirect, url_for,session
from flask import request
from sqlalchemy import create_engine
import random

app = Flask(__name__)
app.secret_key = 'super secret keys'



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
@app.route('/<userName>/climb/')
def climbpage(climbName = None,climb = None,userName = None):
    climbArr = []
    '''
        if('username' in session):
        userName = session['username']
    '''

    # CREATE LIST OF DESIRED CLIMBS FROM DATABASE, EITHER USER OR AREA OR STATE
    climb_names = ['Eagle\'s Nest Traverse', 'Thunderbolt Ridge', 'Sunset Sentinel', 'Peregrine Perch', 'Crimson Crux', 'Majestic Monolith', 'Alpine Ascent', 'Wind Whisper Wall', 'Granite Guardian', 'Serene Summit Spire', 'Cascading Heights Climb', 'Wilderness Wayfarer', 'Sapphire Skyline', 'Echo Edge Expedition', 'Rustic Ridge Rappel', 'Hidden Valley Clamber', 'Vista Vertigo Venture', 'Aurora Apex', 'Daring Dusk Descent', 'Noble Nighthawk Needle', 'Moonlit Mesa Mastery', 'Evergreen Escarpment', 'Whispering Willows Wall', 'Ephemeral Echo Enigma', 'Lunar Labyrinth Leap', 'Sunflower Skyward Scramble', 'Rogue River Ravine', 'Crimson Canyon Climb', 'Mystic Mountain Mirador', 'Pinnacle Ponder Peak', 'Golden Gully Gaze', 'Ethereal Elevation Expedition', 'Starlight Summit Sojourn', 'Celestial Chimney Challenge', 'Ravishing Red Rock Rappel', 'Abyssal Ascent', 'Gossamer Gorge Glide', 'Valiant Valley Vista', 'Jade Jungle Jaunt', 'Cerulean Crest Climb', 'Limestone Labyrinth', 'Copper Creek Chimera', 'Sylvan Skyward Summit', 'Wandering Willow Wall', 'Nebula Nook Nudge', 'Eclipsed Escarpment', 'Dewdrop Delight Descent', 'Rogue Raven Ridge', 'Labyrinthine Ledge', 'Ivory Idyll Incline', 'Verdant Valley Venture', 'Zephyr Zipline Zenith', 'Sunburst Summit Soar', 'Quartz Quarry Quest', 'Frosty Fir Falcon', 'Lunar Leap Ledge', 'Terracotta Terrace Trail', 'Golden Grove Gully', 'Cascade Cradle Climb', 'Amber Ascent Adventure', 'Vivid Vista Venture', 'Crimson Cascade Climb', 'Azure Ascent Ascendancy', 'Moonlit Meadow Mingle', 'Wildflower Wall Wander', 'Marble Monolith Marvel', 'Emerald Enigma Expedition', 'Sunrise Spire Sojourn', 'Lush Lagoon Ledge', 'Twilight Traverse Trail', 'Rustic Rhapsody Rappel', 'Petrified Pine Peak', 'Bountiful Bluff Belay', 'Quicksilver Quest Quell', 'Aether Ascent', 'Cedar Crest Climb', 'Sapphire Summit Sojourn', 'Turbulent Treetop Trek', 'Dusky Descent Drift', 'Frosty Fern Faceoff', 'Peregrine Pinnacle Perch', 'Gossamer Gully Glide', 'Obsidian Outcrop Odyssey', 'Lunar Lull Ledge', 'Rivulet Ridge Rendezvous', 'Aerial Arbor Ascent', 'Stellar Summit Soiree', 'Oaken Overlook Odyssey', 'Onyx Overhang Overture', 'Nebula Niche Nudge', 'Wildwood Wall Whirl', 'Verdant Vortex Venture', 'Celestial Crag Conquest', 'Rustic Ravine Ramble', 'Ethereal Eaves Elevation']

    if(userName):
        for i in range(10):
            climbArr.append(Climb(climb_names[random.randint(0, len(climb_names) - 1)],str(i),str(i),str(i)))
    else:
        for i in range(100):
            climbArr.append(Climb(climb_names[random.randint(0, len(climb_names) - 1)],str(i),str(i),str(i)))

    if(climbArr):
        error = None
    else:
        
        error = "Climbs not Found"
    
    return render_template('climb.html',error=error, climbArr = climbArr,userName = userName)

@app.route('/climb/<climbName>')
def singleClimb(climbName = None):
        error = None
        climb = Climb(climbName,"V4","Boulder","Joshua Tree")
        return render_template('singleClimb.html',climb = climb, error=error)


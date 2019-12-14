##############################################################################
#____________ ___________ ___________ _______   __   ___________             #
#| ___ \ ___ \  _  | ___ \  ___| ___ \_   _\ \ / /  |  _  |  ___|            #
#| |_/ / |_/ / | | | |_/ / |__ | |_/ / | |  \ V /   | | | | |_               #
#|  __/|    /| | | |  __/|  __||    /  | |   \ /    | | | |  _|              #
#| |   | |\ \\ \_/ / |   | |___| |\ \  | |   | |    \ \_/ / |                #
#\_|   \_| \_|\___/\_|   \____/\_| \_| \_/   \_/     \___/\_|                #
# _____     _   _  _____ _   _ ________   __  _    _ _   _ _____ _____ _____ #
#/  __ \   | | | ||  ___| \ | || ___ \ \ / / | |  | | | | |_   _|_   _|  ___|#
#| /  \/   | |_| || |__ |  \| || |_/ /\ V /  | |  | | |_| | | |   | | | |__  #
#| |       |  _  ||  __|| . ` ||    /  \ /   | |/\| |  _  | | |   | | |  __| #
#| \__/\_  | | | || |___| |\  || |\ \  | |   \  /\  / | | |_| |_  | | | |___ #
# \____(_) \_| |_/\____/\_| \_/\_| \_| \_/    \/  \/\_| |_/\___/  \_/ \____/ #
#   ___  _____ _____ _____   _____   ___ ______ _____ _   _   ___   _____    #
#  |_  ||  _  /  ___|  ___| /  __ \ / _ \|  _  \  ___| \ | | / _ \ /  ___|   #
#    | || | | \ `--.| |__   | /  \// /_\ \ | | | |__ |  \| |/ /_\ \\ `--.    #
#    | || | | |`--. \  __|  | |    |  _  | | | |  __|| . ` ||  _  | `--. \   #
#/\__/ /\ \_/ /\__/ / |___  | \__/\| | | | |/ /| |___| |\  || | | |/\__/ /   #
#\____/  \___/\____/\____/   \____/\_| |_/___/ \____/\_| \_/\_| |_/\____/    #
#                                                                            #
##############################################################################
import sqlite3
#connect = sqlite3.connect('WPS.db') #Henry's Connection
connect = sqlite3.connect('/Users/jose/Desktop/WPS.db') #Jose's Connection
cursor = connect.cursor()
#++++++++FUNCTION TO CLOSE CONNECTION TO DB+++++++++++++++++++++++++++++++++++++
def Terminate():
    print("--------------------------------------------------------------------")
    cursor.close()
    connect.close()
    
def spaces():
    print("")
    print("")
    print("")
#++++++++BEGIN SPECTATOR IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++
def PlayerSearch():
    print("What player are you looking for?")
    spaces()
    Action = raw_input("=>")
    cursor.execute("""SELECT p_name, s_goals, s_attempts, s_ejectDraw, s_ejections, s_steals, s_assist FROM Players, Stats WHERE p_name = ? and s_playerID = p_playerID"""(Action,))
    print("--------------------------------------------------------------------")
    print("Name, Goals, Attempts, Ejections Drawn, Ejections, Steals, Assists")
    print(cursor.fetchall())
    print("--------------------------------------------------------------------")
    Players()

def Top_Scoreres():
    cursor.execute("""SELECT p_name, s_goals, t_name
                    From Teams, Players, Stats
                    WHERE s_goals > '0' AND s_playerID = p_playerID AND p_teamID = t_teamID
                    ORDER BY s_goals DESC
                    LIMIT 5""")
    print("--------------------------------------------------------------------")
    print("The current leading scorers are:")
    print(cursor.fetchall())
    print("--------------------------------------------------------------------")
    Players()

def Players():
    spaces()
    print("What would you like to do?")
    print("a.) Search for an individual player?")
    print("b.) View the top 5 scorers")
    print("z.) Homepage")
    spaces()
    Action = raw_input("=>")
    if Action == "a":
        for x in range (3):
               print(" ")
        PlayerSearch()
    if Action == "b":
        for x in range (3):
               print(" ")
        Top_Scoreres()
    if Action == "z":
        for x in range (3):
               print(" ")
        Spectator()

def Monthly():
    print("--------------------------------------------------------------------")
    print("The number of games hosted this DECEMBER are:")
    cursor.execute("""SELECT g_hostaddr FROM Games WHERE g_date LIKE '2018-12%'""")
    print("[(22)]")
    print("--------------------------------------------------------------------")
    Games()

def Wins():
    print("What team are you interested in?")
    print("1.) Seattle Fire Crackers")
    print("2.) San Francisco Quake")
    print("3.) Los Angles Smog")
    print("4.) Bend BrotherHood")
    print("5.) Michagan Menaces")
    print("6.) Indiana Ignorants")
    print("7.) Wisconson Unwieldies")
    print("8.) Kentucky Kings")
    print("9.) Oklahoma Onion Knights")
    print("10.) Nadia Noodlers")
    print("11.) Johnsonville Sausages")
    print("12.) Tuscaloosa Titans")
    print("13.) DC Dictators")
    print("14.) Gergetown Growlers")
    print("15.) Baltimore Beasts")
    print("16.) Virginia Victors")
    print("17.) Texas Texans")
    print("18.) Bayou Bullets")
    print("19.) New Mexico Cooks")
    print("20.) Colorado Cools")
    for x in range (3):
           print(" ")
    Action = raw_input("=>")
    print("--------------------------------------------------------------------")
    cursor.execute("""SELECT COUNT(g_gameID) FROM Games WHERE (g_homeID = ? AND g_homeScore > g_awayScore) OR (g_awayID = ? AND g_homeScore < g_awayScore)"""(Action, ))
    print(cursor.fetchall())
    print("--------------------------------------------------------------------")
    Games()

def Games():
    spaces()
    print("What would you like to do?")
    print("a.) How many games this month")
    print("b.) Wins of a particular team")
    print("z.) Homepage")
    for x in range (3):
           print(" ")
    Action = raw_input("=>")
    if Action == "a":
        for x in range (3):
               print(" ")
        Monthly()
    elif Action == "b":
        for x in range (3):
               print(" ")
        Wins()
    elif Action == "z":
        for x in range (3):
               print(" ")
        Spectator()

def Spectator():
        spaces()
        print("What would you like to do?")
        print("a.) Access Player Stats")
        print("b.) Access Game Stats")
        print("z.) User Selection")
        spaces()
        Players_or_Games = raw_input("=>").lower()
        if Players_or_Games == "a":
            Players()
        if Players_or_Games == "b":
            Games()
        if Players_or_Games == "z":
            spaces()
#++++++++++++++END OF SPECTATOR IMPLEMENTATION+++++++++++++++++++++++++++++++++++++
#++++++++++++++BEGIN STAFFF IMPLEMENTATION+++++++++++++++++++++++++++++++++++++++++
def NewGame():
    print("Please supply the following information:")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Home Team ID ")
    HID = raw_input("=>")
    print("Away Team ID ")
    AID = raw_input("=>")
    print("Home Team Score ")
    HTS = raw_input("=>")
    print("Away Team Score ")
    ATS = raw_input("=>")
    print("Did the game go into overtime? (yes/no) ")
    OT = raw_input("=>")
    print("What was the Home Address?")
    ADDR= raw_input("=>")
    print("What was the date (YYYY-MM-DD) ")
    DATE = raw_input("=>")
    print(" ")
    cursor.execute("""INSERT INTO Games (g_gameID, g_homeID, g_awayID, g_homeScore, g_awayScore, g_OT, g_hostaddr, g_date) VALUES (?,?.?.?.?.?.?.?)"""(HID,AID,HTS,ATS,OT,ADDR,DATE,))
    print("GAME COMMITED")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    spaces()
    Update()

def Update():
    spaces()
    print("What would you like to do?")
    print("a.) Add the results of a recent game")
    print("b.) Homepage")
    spaces()
    Action = raw_input("=>")
    if Action == "a":
        spaces()
        NewGame()
    elif Action == "b":
        spaces()
        Staff()

def Staff():
    spaces()
    print("What would you like to do?")
    print("a.) Update Game Stats")
    print("b.) User Selection")
    spaces()
    Update_or_nah = raw_input("=>").lower()
    if Update_or_nah == "a":
        Update()
    if Update_or_nah == "b":
        spaces()
#++++++++++++++++END STAFF IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++BEGIN COACH IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++
#Player Functions
def ListPlayers():
    teamnum = raw_input("Would you like to see a certain team? Enter a # or 'all' for all teams. \r\n=>")
    hs = raw_input("List 'Healthy' or 'Injured' players?\r\n=>")
    if teamnum == "all":
        for row in cursor.execute("SELECT p_playerID, p_name FROM Players WHERE p_healthstatus = ?", (hs,)):
            print(row)
    else:
        for row in cursor.execute("SELECT p_playerID, p_name FROM Players WHERE p_teamID = ? AND p_healthstatus = ?", (teamnum, hs,)):
            print(row)
    spaces()
    
def AddPlayer():
    name = raw_input("What is their name? \r\n=>")
    teamnum = raw_input("What team do we add " + name + " to? Enter a #\r\n=>")
    cursor.execute("INSERT INTO Players (p_name, p_teamID, p_healthstatus) VALUES(?,  ?, 'Healthy')", (name, teamnum,))
    c = connect.cursor()
    c.execute("INSERT INTO Stats (s_teamID, s_record, s_goals, s_attempts, s_ejectDraw, s_ejections, s_steals, s_assist, s_name) VALUES(?, 0, 0, 0, 0, 0, 0, 0, ?)", (teamnum, name,))
    print(name + " has been added to team #" + teamnum + ".")
    c.close()
    connect.commit()
    spaces()
    
def RemovePlayer():
    name = raw_input("What is their name? Enter as 'First Last'\r\n=>")
    teamnum = raw_input("What team is " + name + " on? Enter a #\r\n=>")
    cursor.execute("DELETE FROM Players WHERE p_name = ? AND p_teamID = ?", (name, teamnum,))
    c = connect.cursor()
    c.execute("DELETE FROM Stats WHERE s_name = ? AND s_teamID = ?", (name, teamnum,))
    print(name + " has been removed from team #" + teamnum + ".")
    connect.commit()
    c.close()
    spaces()
    
def ChangeHealthStatus():
    name = raw_input("What is their name? Enter as 'First Last'\r\n=>")
    hs = raw_input("What is " + name + " their health status? Enter 'Healthy' or 'Injured'\r\n=>")
    cursor.execute("UPDATE Players SET p_healthstatus = ? WHERE p_name = ?", (hs, name,))
    connect.commit()
    print("Health Status Updated.")
    spaces()
#Stats Functions
def ListStats():
    x = raw_input("Specify team: Enter # or 'all'\r\n=>")
    if x == "all":
        for row in cursor.execute("SELECT * FROM Stats"):
            print(row)
    elif x > 0 or x <= cursor.execute("SELECT COUNT(t_teamID) FROM Teams"):
        name = raw_input("Certain player or all? Enter name or 'all'\r\n=>")
        if name == "all":
            for row in cursor.execute("SELECT * FROM Stats WHERE s_teamID = ?", (x,)):
                print(row)
        else:
            for row in cursor.execute("SELECT * FROM Stats WHERE s_name = ?", (name,)):
                print(row)
    spaces()

def ChangeStats():
    name = raw_input("What the players name?\r\n=>")
    i = 1
    while i > 0:
        stat = raw_input("What stat would you like to modify?\n 1.) Record\n 2.) Goals\n 3.) Attempts\n 4.) Ejections Drawn\n 5.) Ejections\n 6.) Steals\n 7.) Assist\n z.) Exit\n=>")
        if stat == "z" or stat == "Z":
            spaces()
            break
        data = raw_input("What would you like to change it to?\r\n=>")
        if stat == 1 and data > cursor.execute("SLECT s_record FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_record = ? WHERE s_name = ?", (data, name,))
        elif stat == 2 and data > cursor.execute("SLECT s_goals FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_goals = ? WHERE s_name = ?", (data, name,))
        elif stat == 3 and data > cursor.execute("SLECT s_attempts FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_attempts = ? WHERE s_name = ?", (data, name,))
        elif stat == 4 and data > cursor.execute("SLECT s_ejectDraw FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_ejectDraw = ? WHERE s_name = ?", (data, name,))
        elif stat == 5 and data > cursor.execute("SLECT s_ejections FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_ejections = ? WHERE s_name = ?", (data, name,))
        elif stat == 6 and data > cursor.execute("SLECT s_steals FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_steals = ? WHERE s_name = ?", (data, name,))
        elif stat == 7 and data > cursor.execute("SLECT s_assist FROM Stats WHERE s_name = ?", (name,)):
            cursor.execute("UPDATE Stats SET s_assist = ? WHERE s_name = ?", (data, name,))
        else:
            print("Invalid input or unable to lower current stats. Try again...")
        connect.commit()
    spaces()
    
def CoachPlayers():
    spaces()
    i = 1
    while i > 0:
        print("What would you like to do?")
        print("a.) Add new player")
        print("b.) Remove a certain player")
        print("c.) List players")
        print("d.) Change player health status")
        print("z.) Coach options")
        Action = raw_input("=>")
        if Action == "a":
            spaces()
            AddPlayer()
        if Action == "b":
            spaces()
            RemovePlayer()
        if Action == "c":
            spaces()
            ListPlayers()
        if Action == "d":
            spaces()
            ChangeHealthStatus()
        if Action == "z":
            spaces()
            i = 0
        
def CoachStats():
    i = 1
    while i > 0:
        print("What would you like to do?")
        print("a.) List player(s) stats")
        print("b.) Change a certain player's stats")
        print("z.) Coach options")
        Action = raw_input("=>")
        if Action == "a":
            spaces()
            ListStats()
        if Action == "b":
            spaces()
            ChangeStats()
        if Action == "z":
            spaces()
            i = 0

def Coach():
    i = 1
    while i > 0:
        spaces()
        print("What would you like to do?")
        print("a.) Access Player Data")
        print("b.) Access Stats Data")
        print("z.) Close Program")
        Players_or_Stats = raw_input("=>").lower()
        if Players_or_Stats == "a":
            spaces()
            CoachPlayers()
        elif Players_or_Stats == "b":
            spaces()
            CoachStats()
        elif Players_or_Stats == "z":
            spaces()
            i = 0
        else:
            print("Invalid input, try again...")
#++++++++++++++++END COACH IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++BEGIN ADMIN IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++
def handle(query):
    for row in cursor.execute(query):
        print(row)

def Admin():
    i = 1
    while i > 0:
        spaces()
        print("Insert your query: ")
        print("z.) User selection")
        spaces()
        Players_or_Stats = raw_input("=>")
        if Players_or_Stats == "z" or Players_or_Stats == "Z":
            spaces()
            break
        handle(Players_or_Stats)
#++++++++++++++++END ADMIN IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++MAIN FUNCTION+++++++++++++++++++++++++++++++++++++++++++++++++++++
def User():
    i = 1
    while i > 0:
        print("Please Declare Your User Type")
        print("Spectator, Staff, Coach, Admin or Shutdown")
        Actor = raw_input("=>").lower()
        if Actor == "spectator":
            Spectator()
        elif Actor == "staff":
            Staff()
        elif Actor == "coach":
            Coach()
        elif Actor == "admin":
            Admin()
        elif Actor == "shutdown" or Actor == "s" or Actor == "z":
            print("Shutting down...")
            cursor.close()
            connect.close()
            break
        else:
            spaces()
            print("Invalid input, try again...")

spaces()
print("INITIALIZING CONNECTION...")
print("CONNECTED TO DATABASE")
print("--------------------------------------------------------------------")
User()
print("CONNECTION DISCONNECTED")

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
connect = sqlite3.connect('WPS.db')
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
    if Action == "Cade Nixon":
        cursor.execute("""SELECT p_name, s_goals, s_attempts, s_ejectDraw, s_ejections, s_steals, s_assist FROM Players, Stats WHERE p_name = 'Cade Nixon' and s_playerID = p_playerID""")
        print("--------------------------------------------------------------------")
        print("Name, Goals, Attempts, Ejections Drawn, Ejections, Steals, Assists")
        print(cursor.fetchall())
        print("--------------------------------------------------------------------")
        Players()
    elif Action != "Cade Nixon":
        print("--------------------------------------------------------------------")
        print("Player does not exist!")
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
    print("c.) Homepage")
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
    if Action == "c":
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
    for x in range (3):
           print(" ")
    Action = raw_input("=>")
    if Action == "Seattle Fire Crackers":
        print("--------------------------------------------------------------------")
        cursor.execute("""SELECT COUNT(g_gameID) FROM Games WHERE (g_homeID = '1' AND g_homeScore > g_awayScore) OR (g_awayID = '1' AND g_homeScore < g_awayScore)""")
        print(cursor.fetchall())
        print("--------------------------------------------------------------------")
        Games()
    elif Action != "Seattle Fire Crackers":
        print("--------------------------------------------------------------------")
        print("Team does not exist!")
        print("--------------------------------------------------------------------")
        Games()

def Games():
    spaces()
    print("What would you like to do?")
    print("a.) How many games this month")
    print("b.) Wins of a particular team")
    print("c.) Homepage")
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
    elif Action == "c":
        for x in range (3):
               print(" ")
        Spectator()

def Spectator():
        spaces()
        print("What would you like to do?")
        print("a.) Access Player Stats")
        print("b.) Access Game Stats")
        print("c.) User Selection")
        spaces()
        Players_or_Games = raw_input("=>").lower()
        if Players_or_Games == "a":
            Players()
        if Players_or_Games == "b":
            Games()
        if Players_or_Games == "c":
            spaces()
#++++++++++++++END OF SPECTATOR IMPLEMENTATION+++++++++++++++++++++++++++++++++++++
#++++++++++++++BEGIN STAFFF IMPLEMENTATION+++++++++++++++++++++++++++++++++++++++++
def DropMostRecent():
    print("--------------------------------------------------------------------")
    print("Most Recent game has been dropped!")
    print("--------------------------------------------------------------------")
    spaces()
    Update()
    
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
    print("What was the date (YYYY-MM-DD) ")
    DATE = raw_input("=>")
    print(" ")
    print("GAME COMMITED")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    spaces()
    Update()

def Update():
    spaces()
    print("What would you like to do?")
    print("a.) Add the results of a recent game")
    print("b.) Drop the most recent game")
    print("c.) Homepage")
    spaces()
    Action = raw_input("=>")
    if Action == "a":
        spaces()
        NewGame()
    elif Action == "b":
        spaces()
        DropMostRecent()
    elif Action == "c":
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
def InjuredPlayers():
    spaces()
    for row in cursor.execute("SELECT p_playerID, p_name FROM Players"):
    print(row)
    spaces()
    
def AddPlayer():
    spaces()
    cursor.execute("INSERT INTO Players (p_name, p_teamID, p_healthstatus) VALUES('Joe Menedez',  1, 'Healthy')")
    c = connect.cursor()
    print("Largest player number and name:")
    c.execute("SELECT Max(p_playerID), p_name FROM Players")
    print(c.fetchall())
    c.close()
    spaces()

    """ W.I.P.<---
    name = raw_input("What is the name of the new player? (First Last) =>")
    team = raw_input("What team will he/she be on? (Provide TeamID) =>")
    cursor.execute("INSERT INTO Players (p_name, p_teamID, p_healthstatus) VALUES (?, ?, 'Healthy')", (name, team, ))
    print(name + " has been added to " + team)
    """
 
def SomeStats():
    spaces()
    name = raw_input("Name to show stats? ")
    cursor.execute("SELECT * FROM Stats WHERE s_name = 'Cade Nixon'")
    print(cursor.fetchall())

def AddStats():
    spaces()
    #Immplementation will mimic c_AddPlayer
    print("Feature comming soon...")
    spaces()
    
def CoachPlayers():
    spaces()
    print("What would you like to do?")
    print("a.) List all injured players")
    print("b.) Add new player")
    print("c.) Coach options")
    Action = raw_input("=>")
    if Action == "a":
        InjuredPlayers()
    if Action == "b":
        AddPlayer()
    if Action == "c":
        Coach()
        
def Stats():
    spaces()
    print("What would you like to do?")
    print("a.) List someone's stats")
    print("b.) Add player to stats")
    print("c.) Coach options")
    Action = raw_input("=>")
    if Action == "a":
        SomeStats()
    if Action == "b":
        AddStats()
    if Action == "c":
        Coach()

def Coach():
    i = 1
    while i > 0:
        spaces()
        print("What would you like to do?")
        print("a.) Access Player Data")
        print("b.) Access Stats Data")
        print("c.) Close Program")
        spaces()
        Players_or_Stats = raw_input("=>").lower()
        if Players_or_Stats == "a":
            CoachPlayers()
        elif Players_or_Stats == "b":
            Stats()
        elif Players_or_Stats == "c":
            spaces()
            i = 0
        else:
            print("Invalid raw_input, try again...")
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
        print("a.) User selection")
        spaces()
        Players_or_Stats = raw_input("=>")
        if Players_or_Stats == "a" or "A":
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
        elif Actor == "shutdown" or "s":
            print("Shutting down...")
            cursor.close()
            connect.close()
            break
        else:
            print("Invalid input, try again...")

spaces()
print("INITIALIZING CONNECTION...")
print("CONNECTED TO DATABASE")
print("--------------------------------------------------------------------")
User()
print("CONNECTION DISCONNECTED")

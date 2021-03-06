
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#--------PROPERTY OF C. HENRY WHITE AND JOSE CADENAS-------------------
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import sqlite3
connect = sqlite3.connect('WPS.db')
cursor = connect.cursor()





#++++++++FUNCTION TO CLOSE CONNECTION TO DB+++++++++++++++++++++++++++++
def Terminate():
    print("Shutting down...")
    print("--------------------------------------------------------------------")
    cursor.close()
    connect.close()
    print("Disconnected from database!!!!!!")







#++++++++BEGIN SPECTATOR IMPLEMENTATION++++++++++++++++++++++++++++++++

def PlayerSearch():
    print("What player are you looking for?")
    for x in range (3):
           print(" ")
    Action = input("=>")
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
    for x in range(3):
        print(" ")
    print("What would you like to do?")
    print("a.) Search for an individual player?")
    print("b.) View the top 5 scorers")
    print("c.) Homepage")
    for x in range (3):
           print(" ")
    Action = input("=>")
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
    Action = input("=>")
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
    for x in range(3):
        print(" ")
    print("What would you like to do?")
    print("a.) How many games this month")
    print("b.) Wins of a particular team")
    print("c.) Homepage")
    for x in range (3):
           print(" ")
    Action = input("=>")
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
        print("What would you like to do?")
        print("a.) Access Player Stats")
        print("b.) Access Game Stats")
        print("c.) Close Program")
        for x in range (3):
            print(" ")
        Players_or_Games = input("=>").lower()
        if Players_or_Games == "a":
            Players()
        if Players_or_Games == "b":
            Games()
        if Players_or_Games == "c":
            Terminate()
            
#++++++++++++++END OF SPECTATOR IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++


#++++++++++++++BEGIN STAFF IMPLEMENTATION+++++++++++++++++++++++++++++++++++++++++++++++
def DropMostRecent():
    print("--------------------------------------------------------------------")
    print("Most Recent game has been dropped!")
    print("--------------------------------------------------------------------")
    for x in range (3):
             print(" ")
    Update()
    
    
def NewGame():
    print("Please supply the following information:")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Home Team ID ")
    HID = input("=>")
    print("Away Team ID ")
    AID = input("=>")
    print("Home Team Score ")
    HTS = input("=>")
    print("Away Team Score ")
    ATS = input("=>")
    print("Did the game go into overtime? (yes/no) ")
    OT = input("=>")
    print("What was the date (YYYY-MM-DD) ")
    DATE = input("=>")
    print(" ")
    print("GAME COMMITED")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    for x in range (3):
             print(" ")
    Update()


def Update():
    print("What would you like to do?")
    print("a.) Add the results of a recent game")
    print("b.) Drop the most recent game")
    print("c.) Homepage")
    for x in range (3):
           print(" ")
    Action = input("=>")
    if Action == "a":
        for x in range (3):
            print(" ")
        NewGame()
    elif Action == "b":
        for x in range (3):
            print(" ")
        DropMostRecent()
    elif Action == "c":
        for x in range (3):
            print(" ")
        Staff()
    

def Staff():
    print("What would you like to do?")
    print("a.) Update Game Stats")
    print("b.) Close Program")
    for x in range (3):
        print(" ")
    Update_or_nah = input("=>").lower()
    if Update_or_nah == "a":
        Update()
    if Update_or_nah == "b":
        Terminate()
        
#++++++++++++++++END STAFF IMPLEMENTATION++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++DRIVER FUNCTION+++++++++++++++++++++++++++++++++++++++++++++++++++
def User():
    print("Please Declare Your User Type (Spectator/Staff)")
    Actor = input("=>").lower()
    if Actor == "spectator":
        Spectator()
    elif Actor == "staff":
        Staff()


print("INITIALIZED VIEW DATA")
print("CONNECTED TO DATABASE")
print("--------------------------------------------------------------------")
User()


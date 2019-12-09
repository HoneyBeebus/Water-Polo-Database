#--------PROPERTY OF C. HENRY WHITE AND JOSE CADENAS-------------------
import sqlite3


connect = sqlite3.connect('WPS.db')
cursor = connect.cursor()

def Terminate():
    print("Shutting down...")
    print("--------------------------------------------------------------------")
    cursor.close()
    connect.close()
    print("Disconnected from database!!!!!!")



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
        Home()

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
        Home()

def Home():
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
            
        


print("INITIALIZED VIEW DATA")
print("CONNECTED TO DATABASE")
print("--------------------------------------------------------------------")
Home()


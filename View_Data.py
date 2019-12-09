#--------PROPERTY OF C. HENRY WHITE AND JOSE CADENAS-------------------
import sqlite3


connect = sqlite3.connect('WPS.db')
cursor = connect.cursor()

def Top_Scoreres():
    cursor.execute("""SELECT p_name, s_goals, t_name
                    From Teams, Players, Stats
                    WHERE s_goals > '0' AND s_playerID = p_playerID AND p_teamID = t_teamID
                    ORDER BY s_goals DESC
                    LIMIT 5""")
    print("The current leading scorers are:")
    print(cursor.fetchall())
    print()

def Players():
    print("What would you like to do?")
    print("a.) Search for an individual player?")
    print("b.) View the top 5 scorers")
    print("c.) Homepage")
    Action = input()
    if Action == "a":
        PlayerSearch()
    if Action == "b":
        Top_Scoreres()
    if Action == "c":
        Home()

def Home():
    print("What would you like to do?")
    print("a.) Access Player Stats")
    print("b.) Access Game Stats")
    print("c.) Close Program")
    for x in range (3):
        print()
    Players_or_Games = input("=>").lower()
    if Players_or_Games == "a":
        Players()
    if 


for x in range (5):
    print()
print("INITIALIZED VIEW DATA")
print("CONNECTED TO DATABASE")
print("--------------------------------------------------------------------")
Home()

cursor.close()
connect.close()
print("Disconnected from database!!!!!!")

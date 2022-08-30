from operator import imod


import random
from urllib import response

print("Welcome to Team Allocator!")



players = ["Mike", "Craig", "Troy", "Zach", "Cody", "Chris","Derek", "Sue", "Claire", 
"Dave", "Alice", "Harry", "Grace", "Rose", "Lexi", "Thomas", "Adriana", "Jean", "James", "Alan"]

while True:

    random.shuffle(players)
    

    team1 = players[:len(players) // 3]

    print("Team 1 captain: " + random.choice(team1))

    print("Team 1:")
    for player in team1: 
        print(player)

    team2 = players[len(players) // 3: (len(players) // 3) * 2]

    print("\nTeam 2 captain: " + random.choice(team2))

    print("Team 2: ")
    for player in team2:
        print(player)
    
    team3 = players[(len(players) // 3) * 2:]

    print("\nTeam 3 captain: " + random.choice(team3))

    print("Team 3:")
    for player in team3:
        print(player)


    response = input("Pick teams again? Type y or n: ")
    if response == "n":
        break



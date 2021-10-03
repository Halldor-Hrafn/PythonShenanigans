import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

x = True

while x == True:
    Name = ["Bjarni","Haukur","Gunnar","Guðrún","Siggi"]
    Win = random.randint(0,4)
    Winner = Name.pop(Win)
    
    print("Til hamingju,",Winner,"Þú vann happdrætti FB!")
    print("Þeir sem unnu ekki eru:",Name)

    Rep = str(input("Viltu draga aftur?"))
    if Rep == "j":
        cls()
        continue
    elif Rep == "n":
        x = False
    else:
        print("I will make you continue against your will")
        continue
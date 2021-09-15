import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = 1

while num01 == 1:
    num02 = int(input("Sláðu inn mánuð sem tölu: "))

    if num02 == 1:
        print("Janúar")
    elif num02 == 2:
        print("Febrúar")
    elif num02 == 3:
        print("Mars")
    elif num02 == 4:
        print("Apríl")
    elif num02 == 5:
        print("Maí")
    elif num02 == 6:
        print("Júní")
    elif num02 == 7:
        print("Júlí")
    elif num02 == 8:
        print("Ágúst")
    elif num02 == 9:
        print("September")
    elif num02 == 10:
        print("Október")
    elif num02 == 11:
        print("Nóvember")
    elif num02 == 12:
        print("Desember")
    else:
        print("Þessi mánuður er ekki til")
        continue
    
    Response = str(input("Viltu halda áfram? "))
    if Response == "j":
        continue
    else:
        break
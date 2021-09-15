import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = 1

while num01 == 1:
    Lengd = int(input("Sláðu inn lengd: "))
    Breidd = int(input("Sláðu inn Breidd: "))
    Haed = int(input("Sláðu inn hæð: "))
    cls()

    print("Flatarmálið er:",Lengd*Breidd)
    print("Ummálið er:",Lengd+Lengd+Breidd+Breidd)
    print("Rúmmálið er:",Lengd*Breidd*Haed)

    Response = str(input("Viltu halda áfram? "))
    if Response == "j":
        continue
    else:
        break
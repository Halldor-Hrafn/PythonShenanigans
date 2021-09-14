import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = 1

while num01 == 1:
    PostNum = int(input("Sláðu inn hvaða póstnúmerið þitt er: "))

    if PostNum >= 101 and PostNum <= 116 and PostNum != 106:
        print("Þú er í reykjavík")
    elif PostNum == 170 and PostNum == 172:
        print("Þú er í Seltjarnarnessi")
    elif PostNum == 190:
        print("Þú er í Vogum")
    elif PostNum >= 200 and PostNum <= 203:
        print("Þú er í Kópavogi")
    elif PostNum == 210 and PostNum == 212:
        print("Þú er í Garðabæ")
    elif PostNum >= 220 and PostNum <= 222:
        print("Þú er í Hafnafjörð")
    elif PostNum == 225:
        print("Þú er í Álftanesi")
    elif PostNum >= 230 and PostNum <= 235 and PostNum != 231:
        print("Þú er í Reykjanesbæ")
    elif PostNum == 260:
        print("Þú er í Reykjanesbæ")
    elif PostNum == 240:
        print("Þú er í Grindavík")
    elif PostNum == 245:
        print("Þú er í Sandgerði")
    elif PostNum == 250:
        print("Þú er í Gerði")
    elif PostNum >= 270 and PostNum <= 271:
        print("Þú er í Mosó")
    elif PostNum == 276:
        print("Þú er í Mosó")
    else:
        print("Þetta póstnúmer er ekki til!")
    response = str(input("Villtu spila aftur? "))
    if response == "j":
        continue
        cls()
    elif response == "n":
        break
    else:
        print("I will make you continue whether you like it or not")
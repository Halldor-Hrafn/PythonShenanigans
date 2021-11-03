import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


num01 = 1

while num01 == 1:
    Rep = int(input("Hversu margar línur viltu? "))

    for i in range(0, Rep):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    Response = str(input("Viltu halda áfram? "))
    if Response == "j":
        continue
        cls()
    else:
        break

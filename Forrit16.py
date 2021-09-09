import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = 200

for i in range (200,149, -1):
    print(i)
    time.sleep(0.1)
time.sleep(2)
cls()

print("So that was part A in this task")
time.sleep(3)

for i in range (50, 100, 5):
    print(i)
    time.sleep(0.1)
time.sleep(2)
cls()

print("That was part B in this task")
time.sleep(3)

num01 = 1
while num01 == 1:
    response = str(input("Sláðu inn eitthvað á lyklaborðið: "))
    if response == "q":
        break
    else:
        print("Þú slóst",response,"á lyklaborðið")

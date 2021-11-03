import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def FaedingarAr(FaedAr):
    print("Þú er fædd...")
    time.sleep(1)
    print(2021-FaedAr)
    time.sleep(2)


num01 = 200

for i in range(200, 149, -1):
    print(i)
    time.sleep(0.1)
time.sleep(2)
cls()

print("So that was part A in this task")
time.sleep(3)

for i in range(50, 105, 5):
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
        cls()
    else:
        print("Þú slóst", response, "á lyklaborðið")

FaedAr = int(input("Sláðu inn hversu gamal þú er: "))
FaedingarAr(FaedAr)

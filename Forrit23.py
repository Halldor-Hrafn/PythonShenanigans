import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


Name = ["Arnar", "Bjarni", "Halldór", "Jón", "Guðmundur",
        "Björn", "Halli", "Jóhan", "Sigga", "María"]
Fjall = "Háfjallaveiki"

sorted(Name)

for x in Name:
    print(x)
time.sleep(2)
cls()

print(Name[5:8])
time.sleep(2)
cls()

print(Name[6:])
time.sleep(2)
cls()

print(Fjall[2:7])
time.sleep(2)
cls()

print(Fjall[8:])
time.sleep(2)
cls()

print(Fjall[0:2], Fjall[8:])
time.sleep(2)

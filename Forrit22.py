import time
import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


Dyr = ["Hundur", "Köttur", "Hamstur", "Naggrís", "Hænur"]
print("Fjöldi dýra í listanum mínnum eru:", len(Dyr))
time.sleep(1)

for i in range(0, 3):
    NewDyr = str(input("Sláðu inn nýt dyr: "))
    Dyr.append(NewDyr)

for x in sorted(Dyr):
    print(x)

time.sleep(3)

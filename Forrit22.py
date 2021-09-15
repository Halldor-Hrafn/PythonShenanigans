import time
import os
import random

Dyr = ["Hundur","Köttur","Hamstur","Naggrís","Hænur"]
print("Fjöldi dýra í listanum mínnum eru:",len(Dyr))
time.sleep(1)

for i in range(0,3):
    NewDyr = str(input("Sláðu inn nýt dyr: "))
    Dyr.append(NewDyr)

sorted(Dyr)

for x in Dyr:
    print(x)

time.sleep(3)
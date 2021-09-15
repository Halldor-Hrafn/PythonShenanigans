import os
import time
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = 1

while num01 == 1:
    Vedur = ["Það verður rok og rigning á morgun","Það verður sól og blíða á morgun",
    "Það verður þurrt en kalt á morgun","Það verður logn með smá skúrum á morgun"]

    num02 = random.randint(0,3)
    print(Vedur[num02])
    
    response = str(input("Viltu heyra aftur? "))
    if response == "j":
        cls()
        continue
    else:
        break
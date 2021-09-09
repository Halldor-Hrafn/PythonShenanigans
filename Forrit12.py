import time
import random
num01 = 1

won = ["Heimalið", "Jafntefli", "Útilið"]

while num01 <= 13:
    print("Liðið sem sigraði leik",num01,"er...")
    time.sleep(1)
    print(won[random.randint(0,2)])
    time.sleep(1)
    num01 = num01+1
    
    if num01 == 13:
        break
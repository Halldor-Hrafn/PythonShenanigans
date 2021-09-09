import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = int(input("Sláðu inn tölu, hvaða tölu sem er: "))
num02 = int(input("Sláðu inn aðra tölu, hvaða tölu sem er: "))
cls()

print("Summa talnanna er:",num01 + num02)
print("Mismunur talnanna er:",abs(num01 - num02))
time.sleep(5)
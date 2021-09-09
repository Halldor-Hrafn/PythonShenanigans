import datetime
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = int(input("Sláðu inn hversu gamal þú er: "))
num02 = 2021-num01

print("Þú ætti vera...")
time.sleep(1)
print("fæddur",num02)
time.sleep(5)
import time
from random import randint
num01 = randint(1, 10)

x = True
while x:
    num02 = int(input("Veldu tölu milli 1-10: "))
    if num02 == num01:
        print("Þú náði rétta tölu!")
        break
    elif num02 < num01:
        print("Aðeins of lágt")
    elif num02 > num01:
        print("Aðeins of stór")

time.sleep(5)

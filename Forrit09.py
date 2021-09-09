import time
num01 = 1

num02 = 0
num03 = 1

while num01 == 1:
    num02 += 1
    if num02 == 5:
        num03 += 1
        num02 = 1
    if num03 == 5:
        break
    print(num03, num02)
    time.sleep(0.5)
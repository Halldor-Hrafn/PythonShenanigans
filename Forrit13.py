import time
import os
import random

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

num01 = random.randint(1,10)

print("Remember this number:",num01)
time.sleep(1)
print("It will be important later")
time.sleep(2)
cls()

while num01 >= 1:
    num02 = int(input("Now, what was the number i told you to remember? "))
    if num02 == num01:
        print("Congrats, you did it")
        break
    else:
        print("That's not the number, try again")

time.sleep(2)

print("Anyways, since my teacher wants to use for loops i want you to input some numbers for me")

while num01 >= 1:
    num03 = int(input("So input a number from 1 to 10 "))
    if num03 > 10:
        print("That number is over 10 you dummy")
        time.sleep(1)
        cls()
        print("Choose another number")
    elif num03 < 1:
        print("That number is less than 1 you dummy")
        time.sleep(1)
        cls()
        print("Choose another number")
    else:
        break

print("Alright, you chose your first number")
time.sleep(0.5)
print("We will do some very boring stuff, but it will be fun to do")
time.sleep(1)
cls()

while num01 >= 1:
    num04 = int(input("So choose a number from 10 to 20 "))
    if num04 < 10:
        print("I said choose a number from 10 to 20 ya dummy")
        time.sleep(1)
        cls()
        print("Pick another number")
    elif num04 > 20:
        print("Smh i said pick a umber from 10 to 20 not 20 to infinity")
        time.sleep(1)
        cls()
        print("Pick another number")
    else:
        break

print("There we go, now we can start using for loops")
time.sleep(0.5)
print("So, what i will show you is the multiplication table of",num03,"And",num04)
num05 = 1
num04 = num04 + 1

for i in range (1,num04):
    print(num03 * num05)
    num05 = num05+1
    time.sleep(0.25)
    if num05 == num04:
        break

time.sleep(10)
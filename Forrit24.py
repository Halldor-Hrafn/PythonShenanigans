import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

x = True
Land = ["Ísland","Bretland","Danmörk","Noreg","Svíðjóð","Finland","Þýskaland","Spán","Frakkland","Portúgal"]

while x:
    num01 = int(input("Hversu mörg lönd viltu bæta við? (amk 5): "))
    if num01 < 5:
        print("Að minsta kost 5 lönd fáviti")
    else:
        for i in range(0,num01):
            Land.append(str(input("Sláðu inn nýt land: ")))
    Land.sort()
    print("Löndin eru:", end=" ")
    for i in Land:
        print(i,end=" ")
    print()
    
    print("Löndin eru:",len(Land))
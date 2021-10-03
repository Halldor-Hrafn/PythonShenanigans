import random

x = True

while x == True:
    Boy = str(input("Sláðu inn stráka nafn: "))
    Girl = str(input("Sláðu inn stelpu nafn: "))

    BoyName = len(Boy)//2
    GirlName = len(Girl)//2

    Chances = random.randint(50,100)
    print("Það eru", str(Chances) + "% líkur að",Boy,Girl,"byrji saman")
    print("Barnið þeira mun heita",Boy[0:BoyName] + Girl[GirlName:])
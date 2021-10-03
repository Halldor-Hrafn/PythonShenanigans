import random

xx = True
x = True
y = True
z = True



while xx == True:
    PlayerOneTotal = 0
    PlayerTwoTotal = 0

    while x == True:
        PlayerOne = random.randint(0,13)
        PlayerTwo = random.randint(0,13)

        print("Spilari 1 dró spilið",PlayerOne)
        print("Spilari 2 dró spilið",PlayerTwo)

        PlayerOneTotal = PlayerOneTotal + PlayerOne
        PlayerTwoTotal = PlayerTwoTotal + PlayerTwo

        print("Spilari 1 er kominn í",PlayerOneTotal)
        print("Spilari 2 er kominn í",PlayerTwoTotal)

        if PlayerOneTotal >= 21:
            print("Spilari 1 sprakk með",PlayerOneTotal)
            RepExit = str(input("Viltu byrja nýjan leik? "))
            if RepExit == "j":
                continue
            else:
                x = False
        elif PlayerTwoTotal >= 21:
            print("Spilari 2 sprakk með",PlayerTwoTotal)
            RepExit = str(input("Viltu byrja nýjan leik? "))
            if RepExit == "j":
                continue
            else:
                x = False
        else:
            while y == True:
                RepOne = str(input("Vill spilari 1 halda áfram? "))
                if RepOne == "j":
                    break
                elif RepOne == "n":
                    print("Spilari 1 hætti með",PlayerOneTotal)
                    xx = False
            
            while z == True:
                RepTwo = str(input("Vill spilari 2 halda áfram? "))
                if RepTwo == "j":
                    break
                elif RepTwo == "n":
                    print("Spilari 2 hætti með",PlayerTwoTotal)
                    xx = False

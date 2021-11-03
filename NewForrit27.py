import random

x = True

while x:
    PlayerOneTotal = 0
    PlayerTwoTotal = 0
    y = True
    PlayerOneRep = "j"
    PlayerTwoRep = "j"

    while y:
        # draw for the players
        if PlayerOneRep == "j":
            OneDraw = random.randint(1, 13)
            PlayerOneTotal = PlayerOneTotal + OneDraw
            print("Spilari 1 dragði", OneDraw)
        if PlayerTwoRep == "j":
            TwoDraw = random.randint(1, 13)
            PlayerTwoTotal = PlayerTwoTotal + TwoDraw
            print("Spilari 2 dragði", TwoDraw)

        print("Spilari 1 er komin með", PlayerOneTotal)
        print("Spilari 2 er komin með", PlayerTwoTotal)

        # check to see if anyone has reached over 21
        if PlayerOneTotal > 21 and PlayerTwoTotal > 21:
            print("Báðir hafa sprungið")
            y = False
        elif PlayerOneTotal > 21:
            print("Spilari 1 hefur sprungið")
            y = False
        elif PlayerTwoTotal > 21:
            print("Spilari 2 hefur sprungið")
            y = False

        # check to see if they want to continue
        if y == True:
            if PlayerOneRep == "j":
                PlayerOneRep = str(input("Spilari 1, villtu halda áfram? "))
            if PlayerTwoRep == "j":
                PlayerTwoRep = str(input("Spilari 2, villtu halda áfram? "))

        # check who won if both said no
        if PlayerOneRep == "n" and PlayerTwoRep == "n":
            if PlayerOneTotal == PlayerTwoTotal:
                print("Það er jafntefli")
                y = False
            elif PlayerOneTotal > PlayerTwoTotal:
                print("Spilari 1 sigraði")
                y = False
            elif PlayerTwoTotal > PlayerOneTotal:
                print("Spilari 2 sigraði")
                y = False

    # check to see if they want to play again
    Respo = str(input("Viltu spila aftur? "))
    if Respo == "n":
        x = False
    print("**********************************")
print("Takk fyrir að spila")

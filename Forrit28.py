x = True


while x == True:
    Word = str(input("Sláðu inn orð: "))
    Letter = str(input("Sláðu inn hvaða bókstaf þú vill að leita af: "))

    print("Strengurin er", Word, "og bókstafurin", Letter,
          "kemur", Word.count(Letter), "sinnum í orðið")
    print(Word[::-1])

    Rep = str(input("Viltu halda áfram? "))
    if Rep == "j":
        continue
    else:
        x = False

x = True

while x == True:
    FullName = str(input("Sláðu inn fullt nafnið þitt: "))
    NameList = FullName.split()

    if len(NameList) >= 2:
        print("Fornafnið þitt er:",NameList[0])
        print("Millinafnið þitt er:",NameList[1])
        print("Eftirnafnið þitt er:",NameList[2])
    elif len(NameList) == 1:
        print("Fornafnið þitt er:",NameList[0])
        print("Eftirnafnið þitt er:",NameList[1])
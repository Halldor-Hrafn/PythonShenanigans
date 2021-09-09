num01 = 1

while num01 >= 1:
    response = str(input("Viltu reikna margfeldi, veldi eða hætta? "))

    if response == "m":
        num02 = int(input("Sláðu inn tölu þú vill að margfalda: "))
        num03 = int(input("Sláðu inn hversu oft þú vill að margfalda: "))
        num03 = num03+1
        num04 = 1

        for i in range (1,num03):
            print(num02 * num04)
            num04 = num04+1
            if num04 == num03:
                break

    if response == "v":
        num02 = int(input("Sláðu inn tölu þú vill að reikna veldi: "))
        num03 = int(input("Sláðu inn hversu oft þú vill að reikna veldið: "))
        num03 = num03+1
        num04 = 1

        for i in range (1,num03):
            print(pow(num02,num04))
            num04 = num04+1
            if num04 == num03:
                break

    if response == "h":
        break
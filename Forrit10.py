num01 = 1

while num01 >= 1:
    num02 = int(input("Sláðu in tölu þú vill sjá marföldunar töfluna af: "))
    num03 = int(input("Sláðu inn hversu oft þú vill margfalda töluna: "))
    num03 = num03+1
    num04 = 1

    for i in range (1,num03):
        print(num02 * num04)
        num04 = num04+1
        if num04 == num03:
            break
    response = str(input("Viltu halda áfram? "))
    if response == "j":
        continue
    elif response == "n":
        break

num01 = 1

while num01 >= 1:
    response = str(input("Viltu reikna margfeldi eða veldi? "))

    if response == "m":
        num02 = int(input("Sláðu inn tölu þú vill að margfalda: "))
        print(num02, "* 1 =", num02 * 1)
        print(num02, "* 2 =", num02 * 2)
        print(num02, "* 3 =", num02 * 3)
        print(num02, "* 4 =", num02 * 4)
        print(num02, "* 5 =", num02 * 5)
        print(num02, "* 6 =", num02 * 6)
        print(num02, "* 7 =", num02 * 7)
        print(num02, "* 8 =", num02 * 8)
        print(num02, "* 9 =", num02 * 9)
        print(num02, "* 10 =", num02 * 10)
        response = str(input("Viltu halda áfram? "))
        if response == "j":
            continue
        elif response == "n":
            break
            num01 = num01-1

    elif response == "v":
        num02 = int(input("Sláðu inn tölu þú vill að sjá í veldi: "))
        print(num02, "Í veldinu 1:", pow(num02, 1))
        print(num02, "Í veldinu 2:", pow(num02, 2))
        print(num02, "Í veldinu 3:", pow(num02, 3))
        print(num02, "Í veldinu 4:", pow(num02, 4))
        print(num02, "Í veldinu 5:", pow(num02, 5))
        print(num02, "Í veldinu 6:", pow(num02, 6))
        print(num02, "Í veldinu 7:", pow(num02, 7))
        print(num02, "Í veldinu 8:", pow(num02, 8))
        print(num02, "Í veldinu 9:", pow(num02, 9))
        print(num02, "Í veldinu 10:", pow(num02, 10))
        response = str(input("Viltu halda áfram? "))
        if response == "j":
            continue
        elif response == "n":
            break
            num01 = num01-1

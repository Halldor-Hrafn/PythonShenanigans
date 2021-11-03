import time
litur = str(input("Sláðu in anað hvort grænn, gulur, eða rauður: "))

if litur == "grænn":
    print("Áfram")
elif litur == "gulur":
    print("Viðbúin")
elif litur == "rauður":
    print("Stopp")
else:
    print("Þú valdi rangan lit. Hvernig dirfist þú.")
time.sleep(5)

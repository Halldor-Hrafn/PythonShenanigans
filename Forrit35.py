file = open('nofn.txt')

Resp = str(input('Sláðu inn nafn til að leitta: '))
IsTrue = False
nameList = []

for line in file:
    word = line.strip()
    nameList = word.split(" ")
    if nameList[0] == Resp:
        print(word)

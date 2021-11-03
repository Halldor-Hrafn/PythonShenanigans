Resp = str(input('Sláðu in eftirnafn: '))
file = open('nofn.txt')
TempList = []

for line in file:
    word = line.strip()
    TempList = word.split(' ')
    if len(TempList) == 3:
        if TempList[2] in Resp:
            print(word)
    elif len(TempList) == 2:
        if TempList[1] in Resp:
            print(word)

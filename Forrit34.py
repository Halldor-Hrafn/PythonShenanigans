file = open('nafn_v34.txt')

Resp = str(input('Sláðu inn nafn til að leitta: '))
IsTrue = False

for line in file:
    word=line.strip()
    if Resp in word:
        print('Nafnið', word ,'fannst í skráni')
        IsTrue = True
if IsTrue == False:
    print('Nafnið fannst ekki')

print('****************************')

file = open('nafn_v34.txt')
nameList = []

for line in file:
    word = line.strip()
    nameList.append(word)

sortedNameList = list(sorted(nameList, key = len))
TempNum01 = len(sortedNameList) - 1

LongestNameLength = len(sortedNameList[TempNum01])
ShortestNameLength = len(sortedNameList[0])

print('Lengsta nafnið er:',sortedNameList[TempNum01])
print('Sttysta nafnið er:',sortedNameList[0])
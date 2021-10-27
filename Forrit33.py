Num01 = 0
Num02 = 0
Encounter = 0
Char01 = 'e'


file = open('words.txt')
for line in file:
    word = line.strip()
    Encounter = Encounter + 1
    if Char01 not in word:
        Num01 = Num01 + 1
    if Char01 in word:
        Num02 = Num02 + 1
print('Það eru %s orð sem eru ekki með "e" í því' % Num01)
print('%.0f'%((Num02/Encounter)*100)+'% orð innihalda stafin e')

print('**************************************')

file = open('words.txt')
Resp = str(input('Sláðu inn bókstaf þú vill ekki að leita af: '))
Num03 = 0
for line in file:
    word = line.strip()
    if Resp not in word:
        Num03 = Num03 + 1
print('Það eru',Num03,'orð ekki með bókstafin',Resp)

print('*****************************')

file = open('words.txt')
Num04 = 0
for line in file:
    word = line.strip()
    Num04 = Num04 + len(word)
print(Num04)


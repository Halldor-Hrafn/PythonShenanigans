file = open('nofn.txt')

eList = []
aList = []

for line in file:
    word = line.strip()
    if 'e' in word:
        eList.append(word)
    if word[2] == 'a':
        aList.append(word)

print('the names with an "e" in them are:', len(eList))
print(aList)
print('The amount of names with "a" as the thrid letter are:', len(aList))

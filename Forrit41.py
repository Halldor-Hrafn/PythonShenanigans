file = open('nofn2.txt')

longName = []
fourName = []

for line in file:
    word = line.strip()
    if len(word) >= 30:
        longName.append(word)
    if word.count(' ') >= 3:
        fourName.append(word)

print(longName)
print('******************************')
print(fourName)
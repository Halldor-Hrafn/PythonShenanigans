file = open('words.txt')
for line in file:
    Word = line.strip()
    if len(Word) >= 20:
        print(Word)

print('********************************')
file = open('words.txt')
nafn = str(input('Sláðu inn nafn þú vilt leita af: '))
for line in file:
    word = line.strip()
    if nafn in word:
        print(word)

print('**************************')
file = open('words.txt')
Num01 = 0
Search = str(input('Sláðu inn staf þú vill að leaita af: '))
for line in file:
    word = line.strip()
    for character in word:
        if character == Search:
            Num01 += 1
print('stafurin', Search, 'kem', Num01, 'sinnum í skjalið')

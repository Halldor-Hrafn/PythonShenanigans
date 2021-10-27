def fornafnLeit():
    FirstName = str(input('Sláðu inn fornafn til að leita af: '))
    file = open('nofn.txt')
    NameList = []

    for line in file:
        word = line.strip()
        NameList = word.split(' ')
        if NameList[0] == FirstName:
            print(word)

def eftirnafnLeit():
    LastName = str(input('Sláðu inn eftirnafn til að leita af: '))
    file = open('nofn.txt')
    NameList = []

    for line in file:
        word = line.strip()
        NameList = word.split(' ')
        if NameList[-1] in LastName:
            print(word)

def forEftirnafnLeit():
    firstName = str(input('Sláðu inn fornafn til að leita af: '))
    lastname = str(input('Sláðu inn eftirnafn til a leita af: '))

print('****************************************')
print('val 1: leita að fornafn')
print('val 2: leita að eftirnafni')
print('val 3: leita að fornafni og eftirnafni')
print('****************************************')
Resp = str(input('veldu eitt: '))

if Resp == 1:
    fornafnLeit()

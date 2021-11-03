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
    file = open('nofn.txt')
    nameList = []

    for line in file:
        word = line.strip()
        nameList = word.split(' ')
        if nameList[0] == firstName:
            x = True
        else:
            x = False
        if x:
            if lastname == nameList[-1]:
                print(word)


def choice():
    print('****************************************')
    print('val 1: leita að fornafn')
    print('val 2: leita að eftirnafni')
    print('val 3: leita að fornafni og eftirnafni')
    print('val 4: hætta í forritið')
    print('****************************************')


x = True
while x:
    choice()
    resp = int(input('veldu eitt: '))

    if resp == 1:
        fornafnLeit()
    elif resp == 2:
        eftirnafnLeit()
    elif resp == 3:
        forEftirnafnLeit()
    elif resp == 4:
        x = False
    else:
        print('pick a valid choice dumbass')

schoolOne = 'Fjölbrautaskóli í Breiðholti'
schoolTwo = 'Menntaskóli í Kópavogi'

fullName = 'Halldór Hrafn Reynisson'

y = True

while y:
    x = True

    print(schoolTwo[0:10],schoolOne[16:])

    for i in fullName:
        print(i, end='+')
    print(' ')

    for i in reversed(fullName):
        print(i, end='')
    print(' ')

    while x:
        response = str(input('Sláðu inn hvaða skóla þú er í: '))
        if response == 'FB':
            print('Þú er í réttn skóla')
            x = False
        else:
            print('You are in the wrong school, FB is better')
    
    startOver = str(input('Villtu spila aftur? '))
    if startOver == 'j':
        continue
    elif startOver == 'n':
        print('Forritið er búið.')
        y = False
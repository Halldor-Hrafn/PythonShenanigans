import random

landList = ['Ísland','Rússland','Bretland','Kanada','Bandaríkin','Danmörk','Þýskaland','Póland','Finland','Svíðjóð']

x = True

print('These are the countries you can visit:', end=' ')
for i in range(0,len(landList)):
    print(landList[i], end=' ')
print( )
print('******************************')

while x:
    resp = int(input('Hversu mörg lönd viltu bætta við listan að ofan? '))
    if resp >= 5:
        print('skrifaðu löndin þú vil bætta við')
        for i in range(0,resp):
            landList.append(str(input('Input a country: ')))
    else:
        print('pick a number over 5 dumbass')
    
    landList.sort()
    for i in range(0, len(landList)):
        print(landList[i])
    x = False

randNum01 = random.randint(0, len(landList)-1)
randNum02 = random.randint(1,10)

print('Þú mun fara til',landList[randNum01],'og vera þar í',randNum02,'vikur')


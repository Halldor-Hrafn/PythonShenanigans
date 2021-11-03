firstName = ['Bjarni', 'Kjartan', 'Sigurður', 'Jón', 'Halldór',
             'Guðmundur', 'Haukur', 'Haraldur', 'Björn', 'Joe']
lastName = ['Jónsson', 'Gunnarsson', 'Aronsson', 'Viðarsson', 'Stefánsson',
            'Halldórsson', 'Guðmundsson', 'Haraldsson', 'Reynirsson', 'Joesson']

for i in range(0, len(firstName)):
    for x in range(0, len(lastName)):
        print(firstName[i], lastName[x])

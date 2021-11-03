import time
from string import ascii_letters, digits


def CharacterCount(String01, String02):
    list01 = []
    for character in String01:
        if character in String02:
            list01.append(character)
    print(list01)
    print(list(set(list01)))


String01 = str(input('Sláu inn streng: '))
String02 = str(input('Sláðu inn annan streng: '))
CharacterCount(String01, String02)

time.sleep(5)

def sumOfNumbers(numList01):
    tempNum = sum(numList01)
    return tempNum


def complicatedCalculationShit(numList01):
    summ = 0
    safnT = []
    for i in range(0, len(numList01)):
        summ += numList01[i]
        safnT.append(summ)
    return summ


def sorter(numList01):
    numList01.sort()
    return numList01


numList01 = []

res = int(input('Hversu margar tölur viltu bætta við listan? '))

for i in range(0, res):
    numList01.append(int(input('Sláðu inn tölu til að bætta við: ')))

sumOfNumbers(numList01)
complicatedCalculationShit(numList01)
sorter(numList01)

print(sumOfNumbers(numList01))
print(complicatedCalculationShit(numList01))
print(sorter(numList01))

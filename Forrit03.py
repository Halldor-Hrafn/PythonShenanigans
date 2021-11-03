import time
isk = int(input("insert how many ISK you want to converte to other currencies: "))
USD = isk/126.61
EURO = isk/148.6
Pound = isk/173.62
DKK = isk/19.98

print(isk, "is equivalent to", round(USD, 2), "USD")
print(isk, "Is equivalent to", round(EURO, 2), "Euros")
print(isk, "Is equivalent to", round(Pound, 2), "Pounds")
print(isk, "Is equivalent to", round(DKK, 2), "DKK")
time.sleep(5)

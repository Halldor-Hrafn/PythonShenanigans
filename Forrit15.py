import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Summa(svar1,svar2):
    print("Summa þessa talna er:",svar1+svar2)
def Mismunur(svar1,svar2):
    print("Mismunur þessa talna er:",abs(svar1-svar2))

svar1 = int(input("Sláðu inn tölu: "))
svar2 = int(input("Sláðu inn aðra tölu: "))

Summa(svar1,svar2)
print("*************************")
Mismunur(svar1,svar2)
time.sleep(3)
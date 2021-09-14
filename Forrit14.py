import datetime
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def FaedingarAr():
    FaedAr = int(input("Sláðu inn hversu gamal þú er: "))
    print("Þú er fædd...")
    time.sleep(2)
    print(2021-FaedAr)
    time.sleep(2)

FaedingarAr()
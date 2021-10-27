import time

LongList = ["Hestur","Api","Kóttur","Hundur","Fíll","Kind","Kú","Hani","Selir","Kissa"]
ShortList = []
TestList = []
Letters = 0

for i in range (0,5):
    ShortList.append(str(input("Sláðu inn nokkur mismunandi dýr: ")))
print("Það eru",len(LongList) + len(ShortList),"dýr í listanum.")

for x in LongList:
    if x in ShortList:
        TestList.append(x)

print("Sama dýrið kom",len(TestList),"sinnum í báðum listum.")

for dyr in LongList:
    Letters += len(dyr)

print("Það eru",Letters,"stafir í dýralistanum")
time.sleep(5)
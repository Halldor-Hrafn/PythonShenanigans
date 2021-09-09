import time
age = int(input("Slæaðu in hversu gamal þú er: "))

if age <= 12: 
    print("Þú ert barn")
if age >= 12 and age <= 20:
    print("Þú ert unglingur")
if age >= 20:
    print("Þú ert fullorðin")

print("Þú var fæddur...",2021-age)
time.sleep(5)
import time

response = str(input("Hvernig ertu í dag? "))

if response.lower() == "gott":
    print("Flott :)")
elif response.lower() == "illa":
    print("Oh neiii :(")
elif response.lower() == "ágætlega":
    print("Það er alveg fínt :)")

time.sleep(5)

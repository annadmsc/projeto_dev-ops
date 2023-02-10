import datetime
today = datetime.datetime.now()
user = input("Whats your name?")


print("Hello " + user + "!")
print("the time is :", today)


# formatting date:


print("today's date is : " + today.strftime("%d-%m-%Y"))
print("the time now is: " + today.strftime("%H-%M-%S"))

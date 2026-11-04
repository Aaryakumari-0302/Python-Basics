year = int(input("Enter Year:"))
if year % 4 == 0 and year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
    print("Leap")
else:
    print("Not leap year")        
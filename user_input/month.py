month=input("Enter Month:")
if month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December":
    print(month," has 31 days")
elif month=="April" or month == "June" or month=="September" or month=="November":
    print(month," has 30 days")
else:
    print("Month has 28 or 29 days")        
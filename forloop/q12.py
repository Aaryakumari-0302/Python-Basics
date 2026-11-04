for i in range(1,101):
    if i%2==0 and i%5==0:
        print(i, "Even and divisible by 5")
    elif i%2==0:
        print(i, "Even")
    else:
        print(i, "Odd")        
def multi(a,b):
    count=0
    for i in range(a,b):
        if i % 11 == 0:
            count=count+1
    print(count)
multi(1,101)
l=[1,2,1,5,7,3]
sec_large=-1
first_large=-1
for i in l:
    if i>first_large:
        sec_large=first_large
        first_large=i
    elif sec_large <i <first_large:
        sec_large=i
    # else:
    #     print("Not Found")
print("First large:",first_large)
print("Second large:",sec_large)        
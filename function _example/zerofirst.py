# l=[0,1,2,0,5,1,3]
# z = []
# zero = []
# for i in l:
#     if i == 0:
#         zero.append(i)
#     else:
#         z.append(i)
# l=(z+zero)
# #print(*l)
# print(l)

#print (ord("a"))
# ch = input("Enter Char:")
# if ord(ch) >= 65 and ord(ch) <=90:
#     print("Uppercase")
# else:
#     print("Lowercase")

year = int(input("Enter Year"))
if year % 4 == 0 and year % 100 != 0:
    print("Leap") 
elif year % 4 == 0 and year % 400 == 0 :
    print("Leap")
else:
    print("Not Leap Year")
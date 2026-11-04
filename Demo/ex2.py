# a = "Mathematics"
# b = len(a)
# for i in range(1,b,2):
#     print(a[i],end=" ")
#print(a[1:b:2])
# for i in range(b):
#     if i%2==1:
#         print(a[i],end=" ")

# s= "College"
# count = 0
# for character in s:
#     if character in "aeiouAEIOU":
#         print(character)
#         count+=1
# print(count)        




balance=10000
operation=input("enter operation ")

if operation=="check balance":
    print(balance)

elif operation =="deposit":
    amount=int(input("enter amount"))
    balance= balance+amount
    print("Balance",balance)
    
elif operation=="withdrawl":
    amount=int(input("enter amount"))
    balance = balance-amount
    print(balance)

elif operation=="exit":
    pass
else:
    print("thank you")
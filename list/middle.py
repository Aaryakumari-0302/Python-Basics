#s = "abcde"
#print(len(s)//2)
#print(s[2])

# i = 0
# j = len(s)-1
# while i <= j:
#     if i == j:
#         print(s[i])
#     i+=1
#     j-=1

s = "abc"
sum = 0
for i in s:
    #print(ord(i))
    sum+=ord(i)
print(sum)

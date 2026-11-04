l = [2,4,8,10]
i = 0
j = len(l)-1
while i < j:
    if i<j:
        l[i],l[j] = l[j], l[i]
    i +=1
    j-=1
print(l)
  

#print(list(reversed(l)))
l = [1,-2,3,-4,-1]
# l.sort()
# print(l)

neg=[]
b=[]
for i in l:
    if i < 0:
        neg.append(i)
    else:
        b.append(i)
print(neg+b)
    

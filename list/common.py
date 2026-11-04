l1=[1,2,3,4,5,6]
l2=[1,3,7,8,2,9]
common=[]
for i in l1:
    if i not in common:
        common.append(i)

for i in l2:
    if i in common:
        print(i)
    else:
        common.append(i)    
print(common)
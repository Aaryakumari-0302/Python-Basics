arrey = [0,1,3]
# for i in range(len(arrey)):
#     if i not in arrey:
#         print(i)
    
c = []
arrey_sum = sum(arrey)
c_sum = 0
for i in range(0,len(arrey)+1):   
    c.append(i)        
print(c)
print(sum(c)-sum(arrey))





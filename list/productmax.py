l = [1,2,8,7,5]
l.sort()
#print(l[-1]*l[-2])
j = len(l)-1
max_product = l[0]*l[0]
for i in l:
    if 0>i<0 or i*j > max_product:
        max_product = i*j
        
print(abs(max_product))
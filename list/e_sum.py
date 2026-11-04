l = [5,3,2,1]
e_sum = 0
o_sum = 0
for i in range (len(l)):
    if i % 2 == 0:
        e_sum = e_sum + l[i]
    else:
        o_sum = o_sum + l[i]
print(e_sum - o_sum)

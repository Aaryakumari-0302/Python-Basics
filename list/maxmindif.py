l=[5,2,6,20,14]
diff=0
max=l[0]
min=1000
for i in l:
    if i > max:
        max = i
print("Max:",max)
for i in l:
    if i < min:
        min = i
print("Min:",min)
diff = max - min
print("Difference: ", diff)

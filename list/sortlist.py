l = [1,3,2,3,5]
sr=[]

for i in range(len(l)-1):
    if l[i]<=l[i+1]:
        sr.append(1)
    else:
        sr.append(0)
print(sr)
if 0 in sr:
    print("Not sorted")
else:
    print("sorted")
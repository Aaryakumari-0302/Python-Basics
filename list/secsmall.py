l=[1,2,1,5,7,3,7]
sec_small=l[-1]
first_small=l[-1]
for i in l:
    if i < first_small:
        sec_small = first_small
        first_small=i
    elif sec_small >i> first_small:
        sec_small = i
print("First Smallest:", first_small)
print("Second Smallest:", sec_small)

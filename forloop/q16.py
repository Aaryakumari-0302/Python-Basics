count1 = 0
count2 = 0
count3 = 0
for i in range(1,101):
    if i%2==0:
        count1+=1
    if i%3==0:
        count2+=1
    if i%5==0:
         count3+=1
print(count1, "Divisible by 2")
print(count2, "Divisible by 3")
print(count3, "Divisible by 5")

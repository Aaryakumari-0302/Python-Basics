# def multi(a,b):
#     count=0
#     for i in range(a,b):
#         if i % 5 == 0 or i % 11 == 0:
#             count=count+1
#     print(count)
# multi(1,51)

l = [2,2,1,1,2]
most = l[0]
count = 0
for i in l:
    c = l.count(i)
    if c > count:
        most = i
       
print("most:", most)
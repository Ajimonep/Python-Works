num=[1,2,2,3,4,5,3,6,4,7]
unique=[]
for i in num:
    if num.count(i)==1:
        unique.append(i)
print(unique)
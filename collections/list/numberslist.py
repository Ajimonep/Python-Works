numbers=[10,11,12,34,43,54,19,78,42]

# for i in range(0,len(numbers)):
#     print(numbers[i])

total=0

for i in range(0,len(numbers)):
    total+=numbers[i]

print("Total=",total)

even_total=0

for i in range(0,len(numbers)):
    if numbers[i]%2==0:
        even_total+=numbers[i]
print("evn total",even_total)

odd_total=0

for i in range(0,len(numbers)):
    if numbers[i]%2!=0:
        odd_total+=numbers[i]


print("sum of odd=",odd_total)
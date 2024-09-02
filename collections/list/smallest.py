number=[3,2,5,7,1,10,4]

smallest_num=number[0]

for i in number:
    if i < smallest_num:
        smallest_num=i

print(f"smallest number={smallest_num}")
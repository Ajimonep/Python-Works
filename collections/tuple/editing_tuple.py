numbers=[1,2,[3,(100,200,300),4],5,6]

num=numbers[2][1]

new_num=list(num)

new_num.insert(1,150)

numbers[2][1]=tuple(new_num)

num3=numbers[2]

poped=num3.pop(2)

newest=num3.insert(1,poped)

print(numbers)
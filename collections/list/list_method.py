num=[1,2,3,4]
num.append(5)#add element to end of list
num.insert(1,6)#add element to a specific position   (1,6) (index,value)
print(num.count(3))#count number of specific element
print(num.pop())#remove and return last element
print(num.pop(3))#remove and return index element
print(num.remove(2))#remove the specific element in thre list in the first occurance of value
print(num.extend([5,7,8,9]))#add a collection of elements to a list
num.sort()
num.reverse()
print(num)

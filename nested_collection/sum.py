arr=[[10,20],[30,40],[50,60]]

num=[num for lst in arr for num in lst]

print(sum(num))
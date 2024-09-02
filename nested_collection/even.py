arr=[
    [10,20],
    [21,30],
    [40,53]
]

even=[num for lst in arr for num in lst if num%2==0]

# print(even)

num_greater_15=[num for lst in arr for num in lst if num>15]

print(num_greater_15)
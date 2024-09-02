arr=[2,3,4,5]

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        if arr[i]+arr[j]==7 and arr[i]!=arr[j]:
            print(arr[i],arr[j])

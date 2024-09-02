num=int(input("enter number \n"))

isPrime=True

for i in range(2,num):
    if num%i==0:
        isPrime=False
        break
print("is prime" if isPrime==True else "Not prime")

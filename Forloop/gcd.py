num2=int(input("enter number"))
num1=int(input("enter number"))
gcd=0

for i in range(2,num1+1):
    if num1%i==0 and num2%i==0:
        gcd=i
print(gcd)
        

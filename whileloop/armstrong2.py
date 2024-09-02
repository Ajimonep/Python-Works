n=int(input("enter number"))

total=0

org=n

count=len(str(n))
while(n!=0):

    digit=n%10

    exponent=digit**count

    total=total+exponent

    n=n//10

print("is armstrong" if total==org else "not armstrong")



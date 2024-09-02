n=int(input("enter number"))

org=n
sum=0

while(n!=0):
    digit=n%10
    sum=sum*10+digit

    n=n//10

print("is palindrome" if sum==org else "not palindrome")

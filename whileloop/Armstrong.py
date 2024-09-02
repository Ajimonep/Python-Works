num=int(input("enter number"))
orginal=num
total=0

digit_count=len(str(num))

while(num!=0):

    digit=num%10

    exponent=digit**digit_count

    total=total+exponent

    num=num//10

    


if orginal==total:
     print(f"{orginal}  is armstrong number")

else:

     print(f"{orginal } is not armstrong number")


num1=int(input("enter number"))
num2=int(input("enter number"))

try:
    result=num1/num2
    print(result)

except Exception as e:
    num2=int(input("enter number2"))
    result=num1/num2
    print(result)

finally:
    print("file tranfer")
    print("db commit")
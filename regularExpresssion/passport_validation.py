from re import fullmatch

passport_number=input("enter number")

pattern="[A-Z][1-9][0-9][0\\s][0-9]{4}[1-9]"

matcher=fullmatch(pattern,passport_number)

print("invalid" if matcher==None else "valid") 
from re import fullmatch

number=input("enter number ")

pattern="(\+91)[\\s]?[6-9][0-9]{9}"

matcher=fullmatch(pattern,number)

print("invalid" if matcher==None else "valid")
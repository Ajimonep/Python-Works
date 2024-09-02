from re import fullmatch

gmail_id=input("enter email id ")

pattern="[A-Za-z0-9][A-Za-z0-9\\._]*(@gmail.com)"

matcher=fullmatch(pattern,gmail_id)

print("invalid " if matcher==None else "valid")
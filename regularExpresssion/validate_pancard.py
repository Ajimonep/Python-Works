from re import fullmatch

card_number=input("enter pan number")

pattern="[A-Z]{3}[PCAFHT][A-Z][0-9]{4}[A-Z]"

matcher=fullmatch(pattern,card_number)

print("invalid" if matcher==None else "valid")
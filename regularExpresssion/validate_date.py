from re import fullmatch

date="31"

pattern="(0?[1-9]|[1-2][0-9]|3[0-1])"
matcher=fullmatch(pattern,date)

print("invalid" if matcher==None else "valid")
from re import fullmatch

month="11"

pattern="(0?[1-9]|1[0-2])"

matcher=fullmatch(pattern,month)

print("invalid" if month==None else "valid")


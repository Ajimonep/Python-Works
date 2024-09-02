from re import finditer

text="abc 7klefg#@"

# pattern="\d"
# pattern="\\D"
# pattern="\w"
# pattern="\\W"
# pattern="\\s"
pattern="\\S"

matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),"==",m.group())
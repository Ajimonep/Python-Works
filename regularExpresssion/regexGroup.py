from re import finditer

text="abc123 @K#7Mdef%&*$"

# pattern="[abd]" check for either a b or d

# pattern="[a-k]"#check for alphebets from a-k

# pattern="[a-z]"#check for alphebets from a-z

# pattern="[A-Z]"all uppercase

# pattern="[A-Za-z]"all alphabets

# pattern="[0-9]"all numbers

# pattern="[a-zA-Z0-9]"

# pattern="[^a-zA-Z0-9]" opposite ,special symbol and space

# pattern="[^A-Za-z]"

pattern="[^(\s)]" #check for space

# pattern="[^a-zA-Z0-9\s]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())
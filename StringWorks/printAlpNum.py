word="i have 2 bike and 1 car"

for ch in word:

    if ch.isalpha():
        print(ch,end=",")
print("\n")
for ch in word:

    if ch.isdigit():
        print(ch,end=",")
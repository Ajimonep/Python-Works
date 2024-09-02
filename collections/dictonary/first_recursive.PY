text="ABCCDDBB"

recursive_count={}

for c in text:
    if c in recursive_count:

        print(c)

        break


    else:
        recursive_count[c]=1




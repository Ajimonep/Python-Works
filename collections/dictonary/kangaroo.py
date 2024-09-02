source="CHICKEN"

target="HEN"

word_count={}

for w in source:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

is_kangaroo=True

for ch in target:

    if ch in word_count and word_count.get(ch)>0:

        word_count[ch]-=1

    else:

        is_kangaroo=False

print(is_kangaroo)



        

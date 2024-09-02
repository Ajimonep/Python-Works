text="ABABCDE"

word_count={}

for w in text:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1


for k,v in word_count.items():

    if v==1:

        print(k)

        
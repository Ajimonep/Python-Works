word="pneumonoultramicroscopicsilicovolcanoconiosis"

vowels="aeiou"

vowel_count=0

consonant_count=0


for ch in word:
    if vowels.count(ch)!=0:
        vowel_count+=1

    else:
        consonant_count+=1

print(consonant_count)


print(vowel_count)



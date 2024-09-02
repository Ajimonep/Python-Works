number=[3,2,5,7,1,11,10,4]

largest=0

secod_largest=0

for i in number:
    if i >largest and i>secod_largest:
        secod_largest=largest
        largest=i

    elif i>secod_largest and i<largest:
        secod_largest=i

print(secod_largest) 
from re import finditer

text="hellopythonhellopythonpythonhello"

matcher=finditer("python",text)

count=0

for m in matcher:
    print(m.start(),"===",m.group())

    count+=1
print(count)
 
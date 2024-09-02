from re import fullmatch


f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\regularExpresssion\\domain.txt")


pattern="[\\w\\W]+\\.com"
for line in f:
    domain=line.rstrip("\n")

    matcher=fullmatch(pattern,domain)

    if matcher!=None:
        print(domain)



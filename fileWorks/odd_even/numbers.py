f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\odd_num.txt","w")
for odd in (50,101):
    if odd%2!=0:
        f.write(str(odd)+"\n")

f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\even_num.txt","w")
for even in (50,101):
    if even%2==0:
        f.write(str(even)+"\n")
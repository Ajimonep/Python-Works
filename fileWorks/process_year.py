f_read=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\years.txt","r")
f_century=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\century.txt","w")
f_noncentury=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\noncentury.txt","w")

for year in f_read:
    
    y=int(year.rstrip("\n"))

    if y%100==0:
        f_century.write(str(y)+"\n")

    else:
        f_noncentury.write(str(y)+"\n")
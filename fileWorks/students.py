f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\students.txt","r")

students=[]

for stud in f:
    students.append(stud.rstrip("\n"))

print(students)
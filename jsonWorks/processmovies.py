from json import load

f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\jsonWorks\\movies.json","r")

films=load(f)

for fl in films:

    print(fl.get("title"))
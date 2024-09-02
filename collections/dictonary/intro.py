students={"name":"Linto","cousrse":"full stack"}

# <class dict> : collection of values in key:value pair

student={"name":"Linto","cousrse":"full stack",'course':"python"}

print(student)

#key should be unique in the key value pair

print(students["name"])

students["name"]="hari"

students["palce"]="chennai"#overwrites the key if the key is present else add as a new pair
print(students)

new=students.items()#
print(new)
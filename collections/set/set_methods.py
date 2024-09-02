names={"hari","hello","chennai"}

name={"hari","hello","chennai","hai","good","morning"}



# names.add("kochi")#to add an element to a set object

# names.clear()#remove elements from list ,empty set remains

# name.pop()#removes random element from a set object

# name.discard("hello")#To remove am element from a set object if its a member in the object

# new_name=["hp","dell","lenovo"]

# name.update(new_name)#add elements from any collection to the set

# new=name.union(new_name)#return the combined elements fro a set and return as anew set

# # print(new)

# new2=name.intersection(names)#returns common elements from the two sets as a new set

# print(new2)

# new3=name.difference(names)

# print(new3)

new4=name.symmetric_difference(names)#combines all elements from two set and remove common element

print(new4)

# print(name)
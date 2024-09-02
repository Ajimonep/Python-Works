from re import fullmatch

f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\regularExpresssion\\vehicleregistration.txt", "r") 
pattern = "(KL)(\\s)?[0-9]{2}(\\s)?[A-Z]{2}(\\s)?[0-9]{4}"
s=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\regularExpresssion\\validvehicleregistration.txt","w")

for line in f:
    reg_num = line.rstrip("\n  ")  
    matcher = fullmatch(pattern, reg_num)

    if matcher!=None:
        s.write(reg_num+"\n")



           
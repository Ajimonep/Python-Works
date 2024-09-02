vehicle_numbers=["kl213456","kl313456","tno10406"]


f=open("C:\\Users\\HP\\Desktop\\PythonLuminarJune\\fileWorks\\vehicle_numbers.txt","w")

for v in vehicle_numbers:
    f.write(v+"\n")
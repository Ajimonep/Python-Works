previous=0
current=1
next=previous+current

while(next<=14) :
    previous=current
    current=next    
    next=next+previous

print(next)


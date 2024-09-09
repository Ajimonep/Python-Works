class opperations:
    def perform_add(self,*args):
        total=sum([arg for arg in args if isinstance(arg,(int,float))])
        return total
         
math=opperations()

print(math.perform_add(10,20,40.4,"hello"))
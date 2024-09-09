class opperations:
    def perform_add(self,*args):
        return sum(args)

    def get_max_numbers(self,*args):
        return max(args)

math=opperations()

print(math.get_max_numbers(10,30,20,15))

print(math.perform_add(10,40,50))
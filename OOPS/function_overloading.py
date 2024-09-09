# def add_numbers(n1,n2):
#     return n1+n2

# def add_numbers(n1,n2,n3):
#     return n1+n2+n3

def add_numbers(*args):
    return sum(args)

print(add_numbers(100,200,300)) 

print(add_numbers(200,300)) 
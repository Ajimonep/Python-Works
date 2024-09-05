class Dishes:
    def __init__(self,name,price,quatity):
        self.name=name
        self.price=price
        self.quatity=quatity

    def __str__(self):
        return self.name

dishe_instance1=Dishes("Biriyani",200,"medium")
dishe_instance2=Dishes("meals",100,"large")
dishe_instance3=Dishes("porota",12,"medium") 

class Restraunt:
    def __init__(self,name,place):
        self.name=name
        self.palce=place
        self.dishes=[]

    def add_dishes(self,dish):
        self.dishes.append(dish)

    def list_dishes(self):
        for d in self.dishes:
            print(d)
restraunt_instance1=Restraunt("alakapuri","kakkanad")           

restraunt_instance1.add_dishes(dishe_instance1)
restraunt_instance1.add_dishes(dishe_instance2)
restraunt_instance1.add_dishes(dishe_instance3)

restraunt_instance1.list_dishes()
class Parent:
    def bike(self):
        print("passion pro")

    def mobile(self):
        print("realme")

class Child(Parent):
    def mobile(self):
        print("iphone")

    def bike(self):
        print("hunter")

Child_instance=Child() 

Child_instance.bike()

Child_instance.mobile()
class Grandparent:
    def m1(self):
        print("class grandparent method m1")

class Parent:
    def m2(self):
        print("class parent method m2")

class child(Parent,Grandparent):
    def m3(self):
        print("child class method m3")

child_instance=child()

child_instance.m3()
child_instance.m2()
child_instance.m1 ()
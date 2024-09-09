class GranndParent:
    def m1(self):
        print("Grandparent class m1 method")

class parent(GranndParent):
    def m2(self):
        print("Parent class m2 method")

class child(parent):
    def m3(self):
        print("child class m3 method")


child_instance=child()

child_instance.m3()
child_instance.m2()
child_instance.m1()
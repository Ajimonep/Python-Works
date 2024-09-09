class Editor:
    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def open(self):
        print(f"{self.name} open")

    def execute(self):
        print(f"{self.name} execute")

class VScode(Editor):
    def __init__(self,name,vendor):
        super().__init__(name,vendor)

vsc_instance=VScode("visual studio code","vscvendor")

vsc_instance.open()

class Pycharm(Editor): 
    def __init__(self,name,vendor):
        super().__init__(name,vendor)

Pycharm_instance=Pycharm("Pycharm","pycharm vendor")
Pycharm_instance.execute()
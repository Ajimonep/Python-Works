from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class Vscode(Editor):
    def open(self):
        print("open editor")

    def execute(self):
        print("execute program")

    def debug(self):
        print("debug program")

class Pycharm(Editor):
    def open(self):
        print("open editor")

    def execute(self):
        print("execute program")

    def debug(self):
        print("debug program")


Pycharm_instance=Pycharm()

Vscode_instance=Vscode()

Vscode_instance.debug()

Pycharm_instance.execute()
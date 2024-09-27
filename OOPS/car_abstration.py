from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def accelarate(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Swift(Car):
    def start(self):
        print("swift start method")

    def accelarate(self):
        print("swift accelarte method")

    def stop(self):
        print("swift stop method")

swift_instance=Swift()

swift_instance.accelarate()
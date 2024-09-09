class Vehicle:
    def start(self):
        print("Vehicle start method")

    def accelarate(self):
        print("Vehicle accelarate method")

class swift(Vehicle):
    pass

swift_instance=swift()

swift_instance.start()

swift_instance.accelarate()
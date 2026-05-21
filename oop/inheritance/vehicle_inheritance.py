class vehicle:

    def __init__(self, brand, speed):
        self.__Brand = brand
        self.__speed = speed

    def get_Brand(self):
        return self.__Brand
    
    def get_speed(self):    
        return self.__speed
    
    def start(self):
        print(self.__Brand + " engine started")

    def stop(self):
        print(self.__Brand + " engine stopped")    

    def display(self):
        print("vechile.brand =" + self.__Brand)
        print("vechile.speed = " + str(self.__speed) + " km/h")

class Car(vehicle):

    def __init__(self, fuel__type, brand, speed):
        self.__fuel_type = fuel__type
        super().__init__(brand, speed)
    
    def display(self):
        print("Car.fuel_type = " + self.__fuel_type)
        super().display()

    def honk(self):
        print(self.get_Brand() + " car is honking")


car1 = Car("Petrol", "Toyota", 180)

car1.display()

print()

car1.start()

car1.honk()

car1.stop()
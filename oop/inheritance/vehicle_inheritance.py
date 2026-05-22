# parent class Vehicle

class Vehicle:

    def __init__(self, brand, speed):
        self.__Brand = brand
        self.__speed = speed

# getter methods

    def get_Brand(self):
        return self.__Brand
    
    def get_speed(self):    
        return self.__speed
    
 # start and stop methods   

    def start(self):
        print(self.__Brand + " engine started")

    def stop(self):
        print(self.__Brand + " engine stopped")    

# display method

    def display(self):
        print("Vehicle.brand =" + self.__Brand)
        print("Vehicle.speed = " + str(self.__speed) + " km/h")

# child class Car inheriting from parent class Vehicle

class Car(Vehicle):

    def __init__(self, fuel_type, brand, speed):
        self.__fuel_type = fuel_type
        super().__init__(brand, speed) # use super() to call the parent class constructor
   
    def honk(self):
        print(self.get_Brand() + " car is honking")

# override the display method to include fuel type information    

    def display(self):
        print("Car.fuel_type = " + self.__fuel_type)
        super().display()

car1 = Car("Petrol", "Toyota", 180)

car1.display()

print()

car1.start()

car1.honk()

car1.stop()
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display_brand(self):
        print("Brand:", self.brand)

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine_type(self):
        print("Engine Type:", self.engine_type)


class Car(Vehicle, Engine):
    def __init__(self, brand, engine_type, color):
        Vehicle.__init__(self, brand)  # Call Vehicle constructor
        Engine.__init__(self, engine_type)  # Call Engine constructor
        self.color = color

    def display_info(self):
        self.display_brand()  # Call Vehicle method
        self.display_engine_type()  # Call Engine method
        print("Color:", self.color)


my_car = Car("Toyota", "Gasoline", "Blue")
your_car = Car("Ferrari" , "Gasoline" , "Red")

my_car.display_info()
your_car.display_info()

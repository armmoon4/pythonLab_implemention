class Superclass:
    def __init__(self):
        self.attribute = "Hello, I am from the superclass."

    def method(self):
        print("This is a method from the superclass.")

class Subclass(Superclass):
    def __init__(self):
        super().__init__()
        self.additional_attribute = "I am from the subclass."

    def additional_method(self):
        print("This is a method specific to the subclass.")

# Creating an instance of the subclass
obj = Subclass()

# Accessing attributes and methods from both the superclass and subclass
print(obj.attribute)
obj.method()
print(obj.additional_attribute)
obj.additional_method()

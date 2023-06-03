class EncapsulationExample:
    def __init__(self):
        self._private_var = None  # Private attribute

    def get_private_var(self):
        return self._private_var

    def set_private_var(self, value):
        self._private_var = value

# Creating an instance of the EncapsulationExample class
example = EncapsulationExample()

# Using the setter method to set the private attribute
example.set_private_var("Hello, Encapsulation!")

# Using the getter method to retrieve the private attribute
print(example.get_private_var())


class EncapsulationExample:
    def __init__(self):
        self.__private_var = "This is a private variable"

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value


example = EncapsulationExample()

print(example.get_private_var())  # Accessing the private variable using the getter method
example.set_private_var("Updated value")  # Modifying the private variable using the setter method
print(example.get_private_var())  # Accessing the updated value of the private variable

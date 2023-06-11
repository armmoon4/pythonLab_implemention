class onlinestore:
    def __init__(self):
        self._private_var = None  # Private attribute

    def get_private_var(self):
        return self._private_var

    def set_private_var(self, value):
        self._private_var = value

example = onlinestore()
example.set_private_var("Hello, python")
print(example.get_private_var())

class onlinestore:
    def __init__(self):
        self.__private_var = "This is a private variable"

    def get_private_var(self):
        return self.__private_var

    def set_private_var(self, value):
        self.__private_var = value


example = onlinestore()

print(example.get_private_var())
example.set_private_var("Updated value")
print(example.get_private_var())

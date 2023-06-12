class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Dog(Animal):
    def make_sound(self):
        print("Woof")

# Creating instances of Cat and Dog
cat = Cat()
dog = Dog()

# Calling the make_sound method
cat.make_sound()  # Output: Meow
dog.make_sound()  # Output: Woof

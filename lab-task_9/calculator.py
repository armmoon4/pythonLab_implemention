class Calculator:
    def calculate(self):
        pass

class Add(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 + self.num2

class Subtract(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 - self.num2

class Multiply(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 * self.num2

class Division(Calculator):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calculate(self):
        return self.num1 / self.num2


add = Add(10,30)
print(add.calculate())

subtract = Subtract(10,5)
print(subtract.calculate())

multiply = Multiply(10,3)
print(multiply.calculate())

division = Division(10,5)
print(division.calculate())
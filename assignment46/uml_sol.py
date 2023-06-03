class mammal:
    _eyecolor = 'none'

    def getcolor(self, color):
        self._eyecolor = color


class Dog(mammal):
    _barkfre = ""

    def bark(self, b):
        self._barkfre = b

    def dis(self):
        print(f"The Dog color-{self._eyecolor} and bark like {self._barkfre}")


class Cat(mammal):
    _meowfre = "none"

    def meow(self, m):
        self._meowfre = m

    def dis(self):
        print(f"The cat color-{self._eyecolor} and call like {self._meowfre}")


ob1 = Dog()
ob1.getcolor("Black")
ob1.bark("Vewvew!")
ob1.dis()
ob2 = Cat()
ob2.getcolor("Red")
ob2.meow("MEOW!")
ob2.dis()
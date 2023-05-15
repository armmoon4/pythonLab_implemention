class AppleBasket:
    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return f"A basket of {self.apple_quantity} {self.apple_color} apples."


# create an instance of AppleBasket and test the methods
basket1 = AppleBasket("red", 4)
print(basket1)  # output: A basket of 4 red apples.
basket1.increase()
print(basket1)  # output: A basket of 5 red apples.


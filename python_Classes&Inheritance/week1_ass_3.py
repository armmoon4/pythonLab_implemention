class BankAccount:
    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return f"Your account, {self.name}, has {self.amt} dollars."


# create an instance of BankAccount
t1 = BankAccount("Bob", 100)

# print the instance using the __str__ method
print(t1)

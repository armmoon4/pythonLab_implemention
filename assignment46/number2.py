class Ecommerce:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        entered_username = input("Username: ")
        entered_password = input("Password: ")

        if entered_username == self.username and entered_password == self.password:
            print("Login successful!")
        else:
            print("Invalid credentials. Login failed.")

    def purchase(self, item):
        print(f"Purchase: {item}")


class ProtectedEcommerce(Ecommerce):
    def login(self):
        print("Login is protected.")

    def purchase(self, item):
        print("Purchase is protected.")


# Creating an instance of the Ecommerce class
ecommerce = Ecommerce("user123", "pass456")
ecommerce.login()
ecommerce.purchase("Item 1")

# Creating an instance of the ProtectedEcommerce class
protected_ecommerce = ProtectedEcommerce("user123", "pass456")
protected_ecommerce.login()
protected_ecommerce.purchase("Item 2")

class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def sort_menu_by_price(menu_items):
        return sorted(menu_items, key=lambda item: item.price)
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price
        return total_price

menu_items = [
    Menu("Coffee 1", 2.99),
    Menu("Coffee 2", 3.99),
    Menu("Coffee 3", 4.99),
]


sorted_menu = Menu.sort_menu_by_price(menu_items)


print("Menu:")
for item in sorted_menu:
    print(f"{item.name}: ${item.price}")

order_id = input("Enter order ID: ")
customer_name = input("Enter customer name: ")
order = Order(order_id, customer_name)

choice = input("Enter 'R' for regular coffee or 'C' for custom coffee order: ")

if choice.upper() == "R":
    # Regular coffee order
    for item in sorted_menu:
        order.add_item(item)
else:
    custom_item = input("Enter custom coffee item name: ")
    custom_price = float(input("Enter custom coffee item price: "))
    order.add_item(Menu(custom_item, custom_price))

print("\nOrder details:")
for item in order.items:
    print(f"{item.name}: ${item.price}")
print("\nOrder delivered!")
print(f"\nOrder {order.order_id} acknowledged.")
feedback = input("Enter customer feedback: ")
rating = int(input("Enter customer rating (1-5): "))
print(f"\nOrder ID: {order.order_id}")
print(f"Customer Feedback: {feedback}")
print(f"Rating: {rating}/5")

class Item:

    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f'Item: {self.name}, {self.description}, {self.dimensions}, {self.price}'


class User:

    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f'customer: {self.name}, {self.surname}, {self.numberphone}'


class Order:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.order_number = user.numberphone[-4:]

    def add_to_order(self, item, qty):
        self.products[item] = qty

    def remove_from_order(self, item):
        qty = self.products.pop(item, None)
        return qty

    def get_item_value(self, item):
        value = item.price * self.products[item]
        return value

    def get_total(self):
        total = 0
        for key, qty in self.products.items():
            total += key.price * qty
        return total

    def __str__(self):
        tmp = ''
        for item, qty in self.products.items():
            tmp += f'{item}: {qty} pcs.\n'
        return f'Order number:{self.order_number} by {self.user} contains:\n{tmp} {self.get_total()} UAH'


item1 = Item('BRIMNES', 79, 'Cabinet with doors', [78, 95])
item2 = Item('IDANAS', 299, 'Wardrobe', [121, 211])
item3 = Item('IKORNEES', 89, 'Floor mirror', [52, 167])
item4 = Item('STUK', 8, 'Cabinet with doorsRoof bag', [34, 51, 28])
# print(item3)
# print(item3.price)

customer1 = User('Ivan', 'Ivanov', '+380502222222')
customer2 = User('Petr', 'Petrov', '+380503333333')
customer3 = User('Sidor', 'Sidorov', '+380504444444')
# print(customer2)
# print(customer2.numberphone)

cart1 = Order(customer3)
cart1.add_to_order(item1, 3)
cart1.add_to_order(item3, 4)
# cart1.remove_from_order(item1)
# cart1.add_to_order(item1, 3)
# print(cart1.get_item_value(item1))
print(cart1, '\n')
# print(cart1.get_total())

cart2 = Order(customer2)
cart2.add_to_order(item2, 4)
cart2.add_to_order(item4, 2)
print(cart2)

assert cart1.get_total() == 593
assert cart2.get_total() == 1212

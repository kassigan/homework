from tkinter.font import names


class Store:

    def __init__(self, name, address, items=None ):
        self.name = name # название магазина
        self.address = address # адрес магазина
        self.items = items if items is not None else {} # "словарь" с товарами


    def add_item(self, name, price):
        self.items[name] = price
        print(f"Item '{name}' is added with the {price}")


    def delete_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f" Item '{name}' has been deleted from the store items")
        else:
            print(f"item '{name}' was not found in the store items")

    def get_price(self, name):
        if name in self.items:
            return self.items[name]
        else:
            print(f"Item '{name}' was not found")
            return None

    def update_price(self,name, new_price):
        if name in self.items:
            old_price = self.items[name]
            self.items[name] = new_price
            print(f"The price of the item '{name}' was changed from {old_price} to {new_price}")
        else:
            print(f"The item '{name}' is not found")



store1 = Store ("Азино", "Комбарская 28",
                {'apples':0.5,
                       'bananas':0.75,
                       'oranges':1.3,
                       'ice-cream':2.0})
store2 = Store ("У бобра", "Пушкинская 240",
                {'bread': 5.9,
                       'eggs': 10.0,
                       'tomatos':3.4})

store3 = Store ("Столичный", "Переулок Гоголя 17")


print(store1.name,store1.address,store1.items)
print(store2.name,store2.address,store2.items)
print(store3.name,store3.address,store3.items)

store3.add_item("pizza", 15.2)
print(store3.name,store3.address,store3.items)

store3.delete_item("pizza")
print(store3.name,store3.address,store3.items)

price = store2.get_price("eggs")
print(price)

store1.update_price("apples", 0.6)
print(store1.name,store1.address,store1.items)

store1.update_price("eggs", 11.2)
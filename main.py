class Item:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                print("Item removed successfully!")
                return
        print("Item not found.")

    def update_item(self, item_id, field, value):
        for item in self.items:
            if item.id == item_id:
                if field == "name":
                    item.name = value
                elif field == "price":
                    item.price = value
                elif field == "quantity":
                    item.quantity = value
                print("Item updated successfully!")
                return
        print("Item not found.")

    def generate_report(self):
        total_value = 0
        print("Inventory Report")
        print("-----------------")
        for item in self.items:
            value = item.price * item.quantity
            total_value += value
            print(f"{item.name} - {item.quantity} units - ${value:.2f}")
        print("-----------------")
        print(f"Total value of inventory: ${total_value:.2f}")

def main():
    inventory = Inventory()
    item1 = Item(1, "Apples", 0.5, 50)
    item2 = Item(2, "Oranges", 0.75, 30)
    inventory.add_item(item1)
    inventory.add_item(item2)

    while True:
        print("Inventory Management System")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Generate report")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            id = int(input("Enter item ID: "))
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = Item(id, name, price, quantity)
            inventory.add_item(item)
            print("Item added successfully!")
        elif choice == "2":
            id = int(input("Enter item ID: "))
            inventory.remove_item(id)
        elif choice == "3":
            id = int(input("Enter item ID: "))
            field = input("Enter field to update (name/price/quantity): ")
            value = input("Enter new value: ")
            inventory.update_item(id, field, value)
        elif choice == "4":
            inventory.generate_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

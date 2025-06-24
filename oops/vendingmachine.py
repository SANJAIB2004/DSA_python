from abc import ABC, abstractmethod

# ------------------ Product Class ------------------
class Item:
    def __init__(self, item_id, name, price, stock):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.item_id}. {self.name} - ₹{self.price} (Stock: {self.stock})"

# ------------------ Abstract User Class ------------------
class AbstractUser(ABC):
    def __init__(self):
        self._balance = 0

    def insert_money(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Balance updated: ₹{self._balance}")
        else:
            print("Invalid amount inserted.")

    def get_balance(self):
        return self._balance

    def deduct_balance(self, amount):
        self._balance -= amount

    def return_change(self):
        if self._balance > 0:
            print(f"Returning change: ₹{self._balance}")
            self._balance = 0

    @abstractmethod
    def view_user_details(self):
        pass

# ------------------ Concrete User Class ------------------
class User(AbstractUser):
    def view_user_details(self):
        print("Regular User: Limited Access")

# ------------------ Admin Class ------------------
class Admin(AbstractUser):
    def __init__(self, password="admin123"):
        super().__init__()
        self.__password = password

    def authenticate(self):
        entered = input("Enter admin password: ")
        return entered == self.__password

    def view_user_details(self):
        print("Admin User: Full Access")

# ------------------ Vending Machine ------------------
class VendingMachine:
    def __init__(self):
        self.items = {
            "1": Item("1", "Chips", 25, 10),
            "2": Item("2", "Coke", 35, 10),
            "3": Item("3", "Candy", 20, 10),
            "4": Item("4", "Water", 15, 10)
        }
        self.__total_cash = 0
        self.user = User()
        self.admin = Admin()

    def display_items(self):
        print("\nAvailable Items:")
        for item in self.items.values():
            print(item)

    def purchase_item(self):
        self.display_items()
        choice = input("Choose item number: ")
        if choice in self.items:
            item = self.items[choice]
            balance = self.user.get_balance()

            if item.stock <= 0:
                print("Item out of stock.")
            elif balance < item.price:
                print(f"Insufficient balance. Insert ₹{item.price - balance} more.")
            else:
                item.stock -= 1
                self.user.deduct_balance(item.price)
                self.__total_cash += item.price
                print(f"Dispensing {item.name}...")
                self.user.return_change()
        else:
            print("Invalid selection.")

    def admin_panel(self):
        if self.admin.authenticate():
            print("\n--- Admin Panel ---")
            self.admin.view_user_details()
            print(f"Total Cash: ₹{self.__total_cash}")
            print("1. Restock Items")
            print("2. Reset Machine")
            option = input("Choose option: ")

            if option == "1":
                for item in self.items.values():
                    item.stock = 10
                print("Restocked all items.")
            elif option == "2":
                self.__total_cash = 0
                print("Machine reset.")
            else:
                print("Invalid option.")
        else:
            print("Wrong password.")

    def run(self):
        while True:
            print("\n--- VENDING MACHINE ---")
            print("1. View Items")
            print("2. Insert Money")
            print("3. Buy Item")
            print("4. Admin Login")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_items()
            elif choice == "2":
                try:
                    amount = int(input("Insert money (₹): "))
                    self.user.insert_money(amount)
                except ValueError:
                    print("Invalid input. Enter a number.")
            elif choice == "3":
                self.purchase_item()
            elif choice == "4":
                self.admin_panel()
            elif choice == "5":
                self.user.return_change()
                print("Thanks for using the vending machine!")
                break
            else:
                print("Invalid choice.")

# ------------------ Main Execution ------------------
if __name__ == "__main__":
    vm = VendingMachine()
    vm.run()

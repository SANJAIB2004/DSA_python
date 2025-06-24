from abc import ABC,abstractmethod

class Item:
    def __init__(self,id,name,price,stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.id} - {self.name} - ₹{self.price} (Stock: {self.stock})"

class AbstractUser(ABC):

    def __init__(self):
        self._balance =0

    def insert_money(self,amount):
        try:
            if amount >0:
                self._balance += amount
                print(f"Balance updated: ₹{self._balance}")
        except Exception as e:
            print(f"Error inserting money: {e}")

    def get_balance(self):
        return self._balance

    def deduct_balance(self,amount):
        try:
            self._balance -= amount
        except Exception as e:
            print(f"Error deducting balance: {e}")

    def return_change(self):
        try:
            if self._balance > 0:
                print(f"Returning change: ₹{self._balance}")
                self._balance = 0
        except Exception as e:
            print(f"Error returning change: {e}")

    @abstractmethod
    def view_user_details(self):
        pass

class User(AbstractUser): # --> concrete Class
    def view_user_details(self):
        print("Regular User: Limited Access")

class Admin(AbstractUser):
    def __init__(self,password="admin123"):
        super().__init__()
        self.__password = password

    def authenticate(self):
        entered = input("Enter admin password: ")
        return entered == self.__password

    def view_user_details(self):
        print("Admin User: Full Access")

class VendingMachine:
    def __init__(self):
        self.items = {
            1: Item(1, "Coke", 50, 10),
            2: Item(2, "Pepsi", 45, 5),
            3: Item(3, "Sprite", 40, 8),
            4: Item(4, "Water", 20, 20),
            5: Item(5,"watermelon juice", 30, 15),
        }
        self.__totalcash =0
        self.users = User()
        self.admin = Admin()

    def display_items(self):
        print("Available Items:")
        for item in self.items.values():
            print(item)

    def purchase_item(self):
        self.display_items()
        try:
            item_id = int(input("Enter the item Id for the item you want to purchase: "))
            if item_id in self.items:
                item = self.items[item_id]
                balance = self.users.get_balance()

            if item.stock <= 0:
                print("Item out of stock.")
            elif balance < item.price:
                print("Insufficient balance.")
            else:
                item.stock -=1
                self.users.deduct_balance(item.price)
                self.__totalcash += item.price
                print(f"Purchased {item.name}. Remaining balance: ₹{self.users.get_balance()}")
        except ValueError:
            print("Invalid input. Please enter a valid item ID.")






if __name__ == "__main__":
    vm = VendingMachine()
    while True:
        print("\nWelcome to the Vending Machine!")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            vm.display_items()
        elif choice == '2':
            try:
                amount = float(input("Enter amount to insert: ₹"))
                vm.users.insert_money(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '3':
            vm.purchase_item()
        elif choice == '4':
            print("Thank you for using the vending machine!")
            break
        else:
            print("Invalid choice. Please try again.")








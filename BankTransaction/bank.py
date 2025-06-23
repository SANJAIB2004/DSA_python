from abc import ABC, abstractmethod

# Abstraction
class BankUser(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


# Encapsulation and Inheritance
class Account(BankUser):
    def __init__(self, name, account_number, balance):
        self._name = name  # Protected attribute
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount!")

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        print("\n===== Account Info =====")
        print(f"Name: {self._name}")
        print(f"Account Number: {self._account_number}")
        print(f"Balance: ₹{self.__balance}")
        print("========================")


# Polymorphism: Overriding Account methods
class Customer(Account):
    def __init__(self, name, account_number, balance):
        super().__init__(name, account_number, balance)

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        super().withdraw(amount)

    def check_balance(self):
        return self.get_balance()


# Menu-Driven Banking System
if __name__ == "__main__":
    print("\nWelcome to the Banking System\n")
    customer = None  # Initialize customer object

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Account Info")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter your name: ")
                account_number = int(input("Enter your account number: "))
                balance = float(input("Enter initial deposit amount: "))
                customer = Customer(name, account_number, balance)
                print("\nAccount Created Successfully!")
                customer.get_account_info()

            elif choice in [2, 3, 4, 5] and customer is None:
                print("\nError: Please create an account first!")

            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                customer.deposit(amount)

            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                customer.withdraw(amount)

            elif choice == 4:
                print(f"Your Current Balance: ₹{customer.check_balance()}")

            elif choice == 5:
                customer.get_account_info()

            elif choice == 6:
                print("Thank you for using the Banking System. Goodbye!")
                break

            else:
                print("Invalid choice! Please enter a valid option.")

        except ValueError:
            print("Error: Please enter a valid number!")

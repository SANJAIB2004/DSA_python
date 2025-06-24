from abc import ABC, abstractmethod

# ------------------ Abstract Base Class ------------------
class AbstractAccount(ABC):
    def __init__(self, account_number, holder_name):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = 0

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn. Remaining Balance: ₹{self._balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def check_balance(self):
        print(f"Account: {self._account_number}, Holder: {self._holder_name}")
        print(f"Balance: ₹{self._balance}")

    def get_balance(self):
        return self._balance

    def get_account_info(self):
        return f"{self._account_number} - {self._holder_name} - ₹{self._balance} - {self.account_type()}"

# ------------------ Derived Classes ------------------
class SavingsAccount(AbstractAccount):
    def account_type(self):
        return "Savings"

class CurrentAccount(AbstractAccount):
    def account_type(self):
        return "Current"

# ------------------ Bank Admin ------------------
class BankAdmin:
    def __init__(self, password="admin123"):
        self._password = password

    def authenticate(self):
        entered = input("Enter admin password: ")
        return entered == self._password

    def view_all_accounts(self, accounts):
        print("\n--- All Accounts ---")
        total = 0
        for acc in accounts:
            print(acc.get_account_info())
            total += acc.get_balance()
        print(f"\nTotal Balance in Bank: ₹{total}")

# ------------------ Banking System ------------------
class BankSystem:
    def __init__(self):
        self.accounts = []
        self.admin = BankAdmin()

    def create_account(self):
        name = input("Enter account holder name: ")
        acc_num = input("Enter account number: ")
        acc_type = input("Enter account type (savings/current): ").lower()

        if acc_type == "savings":
            acc = SavingsAccount(acc_num, name)
        elif acc_type == "current":
            acc = CurrentAccount(acc_num, name)
        else:
            print("Invalid account type.")
            return

        self.accounts.append(acc)
        print(f"{acc_type.capitalize()} account created for {name}.")

    def find_account(self, acc_num):
        for acc in self.accounts:
            if acc._account_number == acc_num:
                return acc
        return None

    def user_operations(self):
        acc_num = input("Enter your account number: ")
        account = self.find_account(acc_num)
        if not account:
            print("Account not found.")
            return

        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                try:
                    amt = float(input("Enter amount to deposit: "))
                    account.deposit(amt)
                except:
                    print("Invalid input.")
            elif choice == "2":
                try:
                    amt = float(input("Enter amount to withdraw: "))
                    account.withdraw(amt)
                except:
                    print("Invalid input.")
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                break
            else:
                print("Invalid choice.")

    def admin_panel(self):
        if self.admin.authenticate():
            self.admin.view_all_accounts(self.accounts)
        else:
            print("Access Denied!")

    def run(self):
        while True:
            print("\n=== Welcome to Python Bank ===")
            print("1. Create Account")
            print("2. Access Account")
            print("3. Admin Panel")
            print("4. Exit")
            choice = input("Select an option: ")

            if choice == "1":
                self.create_account()
            elif choice == "2":
                self.user_operations()
            elif choice == "3":
                self.admin_panel()
            elif choice == "4":
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid option.")

# ------------------ Main Execution ------------------
if __name__ == "__main__":
    bank = BankSystem()
    bank.run()

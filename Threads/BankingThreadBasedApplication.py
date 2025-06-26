import threading
import time

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.condition = threading.Condition()

    def deposit(self, amount):
        with self.condition:
            self.balance += amount
            print(f"{threading.current_thread().name}: Deposited {amount}, New balance: {self.balance}")
            self.condition.notify()  # Notify one waiting thread

    def withdraw(self, amount):
        with self.condition:
            while self.balance < amount:
                print(f"{threading.current_thread().name}: Insufficient balance, waiting...")
                self.condition.wait()  # Wait until deposit is made
            self.balance -= amount
            print(f"{threading.current_thread().name}: Successfully withdrew {amount}, Remaining balance: {self.balance}")

def main():
    account = BankAccount(0)  # Initial balance = 0

    def withdraw_task():
        account.withdraw(1000)

    def deposit_task():
        time.sleep(2)
        account.deposit(2000)

    withdraw_thread = threading.Thread(target=withdraw_task, name="WithdrawThread")
    deposit_thread = threading.Thread(target=deposit_task, name="DepositThread")

    withdraw_thread.start()
    deposit_thread.start()

    withdraw_thread.join()
    deposit_thread.join()

if __name__ == "__main__":
    main()

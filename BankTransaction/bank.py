# to create the banking application with the oops concept in python with adding the money and deducting the money from the account.
# also to check the balance.
0
class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance+=amount
        return self.balance

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return self.balance
        else:
            return "Insufficient Balance"

    def checkbalance(self):
        return self.balance

class Customer(Bank):
    def __init__(self,name,account):
        super().__init__()
        self.name = name
        self.account = account


    def getdetails(self):
        return self.name,self.account


c = Customer("sanjai",4868455)


c.balance = c.deposit(1000)
print(c.checkbalance())
c.balance = c.withdraw(500)
print(c.checkbalance())

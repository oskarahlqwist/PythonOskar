class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

mittkonto = BankAccount()
mittkonto.deposit(100)

mittkonto2 = BankAccount()
mittkonto2.deposit(100)
mittkonto.withdraw(20)

print(mittkonto.balance, mittkonto2.balance)
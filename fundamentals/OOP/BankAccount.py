class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"${self.balance}")

    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self


jonel = BankAccount(0.01, 100)
jonathan = BankAccount(0.01, 500)

jonel.deposit(100).deposit(100).deposit(100).withdraw(
    50).yield_interest().display_account_info()

jonathan.deposit(350).deposit(350).withdraw(25).withdraw(25).withdraw(
    50).withdraw(100).yield_interest().display_account_info()

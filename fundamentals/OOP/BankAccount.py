class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        balance = 0
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"${self.balance}")

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
        return self

    @classmethod
    def all_banks_info(cls):
        print("Printing All Bank Account Info")
        for account in cls.all_accounts:
            account.display_account_info()


jonel = BankAccount(0.01, -400)
jonathan = BankAccount(0.01, 500)

jonel.deposit(100).deposit(100).deposit(100).withdraw(
    50).yield_interest().display_account_info()

jonathan.deposit(350).deposit(350).withdraw(25).withdraw(25).withdraw(
    50).withdraw(100).yield_interest().display_account_info()

BankAccount .all_banks_info()

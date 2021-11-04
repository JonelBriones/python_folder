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
            self.balance -= (5 + amount)
            print("Insufficient funds: Charging a $5 fee")

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
# above line is BankAccount


class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        return(f"User: {self.name}, Balance: ${self.account.balance}")

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        print((self.display_user_balance()))
        print((other_user.display_user_balance()))


jonel = User("Jonel Briones", "ijonel906@gmail.com")
john = User("John-John Briones", "john-john@gmail.com")
jonathan = User("Jonathan Briones", "jonathan@gmail.com")

jonel.make_deposit(500).make_deposit(100).make_deposit(
    75).make_withdrawal(680).display_user_balance()
print(jonel.display_user_balance())

john.make_deposit(101).make_deposit(
    200).make_withdrawal(300).display_user_balance()
print(john.display_user_balance())

jonathan.make_deposit(1000).make_withdrawal(
    200).make_withdrawal(400).make_withdrawal(50).display_user_balance()
print(jonathan.display_user_balance())


jonel.transfer_money(jonathan, 5)

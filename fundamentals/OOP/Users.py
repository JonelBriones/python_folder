class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method

    def make_deposit(self, amount):  # takes an argument that is the amount of the deposit
        # the specific user's account increases by the amount of the value received
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, account_balance):
        self.account_balance -= account_balance
        other_user.account_balance += account_balance
        print((self.display_user_balance()))
        print((other_user.display_user_balance()))


jonel = User("Jonel Briones", "ijonel906@gmail.com")
john = User("John-John Briones", "john-john@gmail.com")
jonathan = User("Jonathan Briones", "jonathan@gmail.com")

jonel.make_deposit(50).make_deposit(100).make_deposit(
    75).make_withdrawal(200).display_user_balance()
print(jonel.display_user_balance())

john.make_deposit(101).make_deposit(
    200).make_withdrawal(300).display_user_balance()
print(john.display_user_balance())

jonathan.make_deposit(1000).make_withdrawal(
    200).make_withdrawal(400).make_withdrawal(50).display_user_balance()
print(jonathan.display_user_balance())


jonel.transfer_money(jonathan, 5)

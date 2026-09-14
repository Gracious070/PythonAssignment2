class BankAccount:

    def __init__(self, balance):
        # Double underscore is used for the private balance attribute.
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful.")
        else:
            print("Withdrawal failed.")

    def display_balance(self):
        print("Current balance:", self.__balance)


# Create a BankAccount object.
account = BankAccount(1000)

# Change and view the balance through methods.
account.deposit(500)
account.withdraw(200)
account.display_balance()
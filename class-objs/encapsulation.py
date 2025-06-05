class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder  # Protected attribute
        self.__balance = initial_balance      # Private attribute

    # Getter method for balance
    def get_balance(self):
        return self.__balance

    # Setter method for balance with validation
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount")

    # Getter for account holder (read-only property)
    def get_account_holder(self):
        return self._account_holder


# Using the BankAccount class
account = BankAccount("Alice", 1000)
print(f"Account holder: {account.get_account_holder()}")
print(f"Initial balance: ${account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  # Should fail
account.set_balance(-100)  # Should fail
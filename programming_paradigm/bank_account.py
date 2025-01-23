
class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance.
        :param initial_balance: Starting balance of the account (default is 0).
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: True if withdrawal was successful, False otherwise.
        """
        if amount > 0 and self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")

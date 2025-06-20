class BankAccount:
    """A simple bank account class that supports deposit withdraw and balance display."""

    def __init__(self, initial_balance=0.0):
        """Initialise the account with an optional initial balance."""
        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Initial balance must be a numeric value")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be numeric")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._account_balance += amount

    def withdraw(self, amount):
        """Withdraw a positive amount from the account if sufficient funds exist return True otherwise False."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be numeric")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._account_balance:
            return False
        self._account_balance -= amount
        return True

    def display_balance(self):
        """Print the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")

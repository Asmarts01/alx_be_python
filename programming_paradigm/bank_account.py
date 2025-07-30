# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money from the account if sufficient funds exist."""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current balance: ${self.account_balance:.2f}")

# main.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Starting balance: $100

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit:<amount>, withdraw:<amount>, display")
        sys.exit(1)

    command_input = sys.argv[1]
    
    if ':' in command_input:
        command, param = command_input.split(':', 1)
        try:
            amount = float(param)
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            sys.exit(1)
    else:
        command = command_input
        amount = None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Please use deposit:<amount>, withdraw:<amount>, or display.")

if __name__ == "__main__":
    main()
# This code defines a simple bank account management system.
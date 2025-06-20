import sys
from bank_account import BankAccount

def main():
    try:
        account = BankAccount(100.0)
    except (TypeError, ValueError) as e:
        print(f"Error initialising account: {e}")
        sys.exit(1)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit withdraw display")
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
    except ValueError:
        print("Error: Amount must be a numeric value")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount}")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            succeeded = account.withdraw(amount)
            if succeeded:
                print(f"Withdrew: ${amount}")
            else:
                print("Insufficient funds")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

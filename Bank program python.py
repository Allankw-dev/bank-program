import json
import os
from decimal import Decimal, InvalidOperation
from datetime import datetime


class BankAccount:
    def __init__(self, filename="account.json"):
        self.filename = filename
        self.balance = Decimal('0.00')
        self.transactions = []
        self.pin = None
        self.load_data()

    def load_data(self):
        """Load account data from file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    data = json.load(f)
                    self.balance = Decimal(str(data.get('balance', '0.00')))
                    self.transactions = data.get('transactions', [])
                    self.pin = data.get('pin')
            except Exception as e:
                print(f"⚠️ Error loading data, resetting account: {e}")
                self.balance = Decimal('0.00')
                self.transactions = []
                self.pin = None
                self.save_data()

    def save_data(self):
        """Save account data to file"""
        try:
            data = {
                'balance': str(self.balance),
                'transactions': self.transactions,
                'pin': self.pin
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"⚠️ Error saving data: {e}")

    def authenticate(self):
        """Require user to set or enter a PIN (PyCharm-friendly)"""
        if self.pin is None:
            while True:
                print("💳 No PIN set. Please create a 4-digit PIN.")
                new_pin = input("Enter new PIN: ")
                confirm_pin = input("Confirm PIN: ")
                if new_pin == confirm_pin and new_pin.isdigit() and len(new_pin) == 4:
                    self.pin = new_pin
                    self.save_data()
                    print("✅ PIN set successfully!\n")
                    break
                else:
                    print("❌ PINs do not match or invalid. Try again.")
        else:
            attempts = 3
            while attempts > 0:
                entered = input("Enter your PIN: ")
                if entered == self.pin:
                    print("✅ PIN verified. Welcome!\n")
                    return True
                else:
                    attempts -= 1
                    print(f"❌ Incorrect PIN. {attempts} attempt(s) left.")
            print("🚫 Too many wrong attempts. Exiting.")
            exit()

    def sanitize_input(self, amount_str):
        """Clean user input to remove $ or commas"""
        try:
            clean = amount_str.replace('$', '').replace(',', '').strip()
            return Decimal(clean)
        except (InvalidOperation, AttributeError):
            return None

    def show_balance(self):
        print(f"\n{'='*40}")
        print(f"💰 Your current balance: ${self.balance:.2f}")
        print(f"{'='*40}")

    def deposit(self):
        amount_str = input("Enter amount to deposit: $")
        amount = self.sanitize_input(amount_str)
        if amount is None or amount <= 0:
            print("❌ Invalid amount! Must be a positive number.")
            return

        self.balance += amount
        transaction = {
            'type': 'DEPOSIT',
            'amount': float(amount),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'balance_after': float(self.balance)
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"✓ Deposit successful! New balance: ${self.balance:.2f}")

    def withdraw(self):
        amount_str = input("Enter amount to withdraw: $")
        amount = self.sanitize_input(amount_str)
        if amount is None or amount <= 0:
            print("❌ Invalid amount! Must be a positive number.")
            return

        if amount > self.balance:
            print(f"❌ Insufficient balance! Available: ${self.balance:.2f}")
            return

        self.balance -= amount
        transaction = {
            'type': 'WITHDRAWAL',
            'amount': float(amount),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'balance_after': float(self.balance)
        }
        self.transactions.append(transaction)
        self.save_data()
        print(f"✓ Withdrawal successful! New balance: ${self.balance:.2f}")

    def show_history(self):
        if not self.transactions:
            print("\n❌ No transactions yet!")
            return

        print(f"\n{'='*70}")
        print(
            f"{'Transaction Type':<15} {'Amount':<12} {'Balance':<12} {'Date & Time':<25}")
        print(f"{'='*70}")

        for txn in self.transactions:
            print(
                f"{txn['type']:<15} ${txn['amount']:<11.2f} ${txn['balance_after']:<11.2f} {txn['timestamp']:<25}")

        print(f"{'='*70}")

    def run(self):
        print("\n" + "="*40)
        print("   🏦 Welcome to Bank Account Program")
        print("="*40)

        self.authenticate()

        while True:
            print("\n1. Show balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ").strip()

            if choice == "1":
                self.show_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                self.show_history()
            elif choice == "5":
                print("\n✓ Thank you for using Bank Program. Goodbye!")
                break
            else:
                print("❌ Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    account = BankAccount()
    account.run()

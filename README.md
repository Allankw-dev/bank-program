# bank-program
🏦 Bank Account Management System

A console-based bank account management system in Python that allows users to deposit, withdraw, view balance, and track transaction history. All account data is persistently stored in a JSON file.

This version includes PIN authentication and improved input handling for PyCharm and other IDEs.

✨ Features

💰 Check Balance – Display your current account balance

🏦 Deposit Funds – Add money to your account

💸 Withdraw Funds – Withdraw money with automatic balance check

📜 Transaction History – View all transactions with type, amount, balance, and timestamp

🔐 PIN Authentication – Secure your account with a 4-digit PIN

📂 Persistent Storage – All data saved automatically in account.json

🎨 User-Friendly Console Interface – Clear formatting, readable messages

🛡️ Input Validation – Accepts $ and comma-formatted numbers

⚡ Installation
Prerequisites

Python 3.6+ installed

Optional: Git to clone the repository

Steps

Clone the repository or download the project:

git clone <repository-url>


Navigate to the project folder:

cd bank-account-program


Run the program:

python bank_account.py

📝 Usage

Set or enter your PIN at startup:

If no PIN exists, you’ll be prompted to create one.

Enter a 4-digit PIN to secure your account.

Main menu options:

1. Show balance
2. Deposit
3. Withdraw
4. Transaction History
5. Exit


Select the option by entering 1-5.

For deposits and withdrawals, enter the amount when prompted.

Transactions are automatically saved to account.json.

Example

Depositing $500:

Enter amount to deposit: $500
✓ Deposit successful! New balance: $500.00


Viewing Transaction History:

Transaction Type   Amount       Balance      Date & Time
DEPOSIT            $500.00      $500.00      2026-02-15 15:42:10

📁 File Structure
bank_account.py      # Main program script
account.json         # JSON file storing balance, transactions, and PIN
README.md            # Project documentation

🚀 Future Improvements

🖥️ GUI Interface – Build a graphical version with Tkinter or PyQt

📆 Interest & Fees – Add monthly interest or transaction fees

🔍 Transaction Filters – Sort or filter transactions by type, date, or amount

🔐 Advanced Security – Hash PINs for extra security

📜 License

This project is open-source and available under the MIT License.

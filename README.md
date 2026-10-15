# bank-program

🏦 Secure Bank Account Management System.

A secure, console-based banking system built with Python that allows users to manage their account balance, perform transactions, and securely authenticate using a 4-digit PIN.

This project demonstrates:

- Object-Oriented Programming (OOP)
- File persistence using JSON
- Secure authentication logic
- Input validation and error handling
- Professional code structure

## 📌 Project Overview

This application simulates a simple banking system where users can:

- View account balance
- Deposit funds
- Withdraw funds (with balance validation)
- View full transaction history
- Secure their account using a PIN

All account data is stored locally in a structured JSON file.

## 🚀 Features

### 🔐 Security

- 4-digit PIN authentication
- 3 login attempts before exit
- PIN stored persistently

### 💰 Financial Operations

- Accurate money calculations using Decimal
- Deposit validation (positive amounts only)
- Withdrawal validation (prevents overdraft)

### 📂 Data Persistence

Automatically saves:

- Balance
- Transaction history
- PIN

Uses `account.json`.

### 🧾 Transaction Logging

Each transaction stores:

- Type (Deposit/Withdrawal)
- Amount
- Timestamp
- Balance after transaction

### 🛡 Input Handling

Accepts:

- `$500`
- `1,000`
- `1000`

Prevents invalid numeric input.

## 🛠 Technologies Used

- Python 3
- `json` module
- `decimal` module (for financial precision)
- `datetime`
- Object-Oriented Programming principles

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Allankw-dev/bank-program.git
```

### 2️⃣ Navigate Into Project Folder

```bash
cd bank-program
```

### 3️⃣ Run the Program

```bash
python "Bank program.py"
```

Works perfectly in:

- ✅ PyCharm
- ✅ VS Code
- ✅ Command Prompt / Terminal

## 🖥 Program Flow

1. User sets or enters a 4-digit PIN
2. Main menu appears
3. User selects an option (1–5)
4. Data is automatically saved after every transaction

## 📁 Project Structure

```
📦 bank-program
┣ 📜 Bank program.py
┣ 📜 account.json   (created automatically on first run)
┣ 📜 LICENSE
┗ 📜 README.md
```

## 🧠 What This Project Demonstrates

✔ Clean OOP design
✔ Real-world financial logic
✔ Data persistence
✔ Error handling
✔ User authentication
✔ Clean console UI formatting

This makes it a strong beginner-to-intermediate portfolio project.

## 🔮 Future Improvements

- 🔐 Hash PIN instead of storing plain text
- 🖥 Add graphical user interface (Tkinter)
- 🌐 Convert to web app (Flask/Django)
- 📊 Add spending analytics
- 🏦 Multi-user account support

## 📜 License

This project is open-source and available under the MIT License.

## 👨‍💻 Author

Allan Kamau
Aspiring Software Developer
GitHub: [Allankw-dev](https://github.com/Allankw-dev)

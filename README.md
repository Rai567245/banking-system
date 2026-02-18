## 🏦 RGBC ATM Transaction System (Python)

A console-based ATM system built in Python as a midterm case study for Computer Programming 2 (COMPROG2).
This project demonstrates the application of Object-Oriented Programming (OOP) concepts such as classes, objects, encapsulation, constructors, inheritance, polymorphism, and exception handling, using a real-world banking scenario.

## 📌 Project Overview

The RGBC (Richard Gwapo Banking Corporation) ATM System simulates basic banking transactions such as:

  - Secure user login using account number and PIN
  - Balance inquiry
  - Withdrawal
  - Deposit
  - Fund transfer
  - Account blocking after multiple failed PIN attempts

The system uses predefined bank accounts stored in an array/list and enforces transaction rules similar to real ATM machines.

## 🎯 Objectives

  - Apply Object-Oriented Programming principles in Python
  - Simulate real ATM transaction workflows
  - Implement input validation and exception handling
  - Practice encapsulation and data protection
  - Handle user errors and invalid transactions properly

## 🧱 Features

1. 🔐 Login System

  - Login using Account Number and PIN
  - Maximum of 3 incorrect PIN attempts
  - Account is automatically blocked after 3 failed attempts
  - Blocked accounts cannot transact unless reactivated by an administrator

2. 💳 Supported Transactions

  Transaction	Description: 

  - Balance Inquiry	View account number, name, and current balance
  - Withdrawal	Withdraw money (minimum ₱100, 100-denomination only)
  - Deposit	Deposit money (minimum ₱100)
  - Transfer Fund	Transfer money to another valid account
  - Cancel	Exit transaction menu

3. 💸 Transaction Rules

  I. Withdrawal

  - Minimum amount: ₱100
  - Must be divisible by 100
  - Cannot exceed available balance

  II. Deposit

  - Minimum deposit: ₱100
  - Accepts decimal values
  - Transfer Fund
  - Minimum transfer: ₱1000
  - ₱25 service fee for every ₱1000 transferred
  - Recipient account must exist
  - Must have sufficient balance (including fees)

4. 🗂 Sample Account Data

Account Number	Account Name	    Balance	  PIN	  Status
0123-4567-8901	Roel Richard	    5000.00	  1111	Active
2345-6789-0123	Dorie Marie	      0.00	    2222	Blocked
3456-7890-1234	Railee Darrel	    10000.00	3333	Active
4567-8901-2345	Railynne Dessirei	2500.00	  4444	Active
5678-9012-3456	Raine Dessirei	  10000.00	5555	Active

5. 🧠 OOP Concepts Used

- I. Classes & Objects – Account, ATM, Transaction classes
- II. Encapsulation – Protected account details
- III. Constructors – Initialize account data
- IV. Inheritance – Transaction types
- V. Polymorphism – Different transaction behaviors
- VI. Exception Handling – Invalid input, insufficient funds, blocked accounts

## ▶️ How to Run the Program

  1. Make sure Python is installed

    - python --version

  2. Clone the repository

    - git clone https://github.com/your-username/rgbc-atm-system.git

  3. Navigate to the project folder

    - cd rgbc-atm-system
  
  4. Run the program
  
    - python main.py
  
## 🧪 Sample Flow

  1. Start program
  2. Choose S to start transaction or Q to quit
  3. Enter account number and PIN
  4. Select transaction type
  5. Perform transaction
  6. Return to menu or exit

## 📁 Branch Tree Example

    banking-system/
    │
    ├── docs/
    │   ├── scope_&_limitations.md
    │   └── transaction_rules.md
    │
    ├── features/
    │   ├── feature_account_system/
    │   │   ├── __init__.py
    │   │   ├── account_list.py
    │   │   ├── account_system.py
    │   │   └── README.md
    │   │
    │   ├── feature_balance_inquiry/
    │   │   ├── balance_inquiry_feature.py
    │   │   └── README.md
    │   │
    │   ├── feature_deposit/
    │   │
    │   ├── feature_login_auth/
    │   │   ├── __init__.py
    │   │   ├── login_authentication_feature.py
    │   │   └── README.md
    │   │
    │   ├── feature_transaction_menu/
    │   │   ├── transaction_menu_feature.py
    │   │   └── README.md
    │   │
    │   ├── feature_transfer_funds/
    │   │
    │   └── feature_withdrawal/
    │       ├── __init__.py
    │       ├── withdrawal_feature.py
    │       └── README.md
    │
    ├── testing/
    │
    ├── utils/
    │   ├── __init__.py
    │   ├── banner_ui.py
    │   ├── center_text_ui.py
    │   ├── left_text_ui.py
    │   └── terminal_ui.py
    │
    └── main.py

## 🚀 Future Improvements

  - Admin panel for account activation
  - File or database storage (MySQL / SQLite)
  - GUI version using Tkinter or PyQt
  - Transaction history logging

## 📚 Academic Context

This project was developed as a Midterm Case Study for:
  - COMPROG2 – Computer Programming 2, focusing on Object-Oriented Programming with exception handling.

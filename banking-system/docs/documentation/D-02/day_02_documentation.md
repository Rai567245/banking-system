# 📘 Day 02 Documentation

## Project: Banking System (Console-Based, Python)

### 📅 Date

Day 01 – System Setup & Login Authentication Feature

### 🎯 Objective for Day 02

The main goal for Day 02 was to initialize the project structure and implement the Login Authentication feature for the banking system. This serves as the foundation for all future system features.

### 🗂️ Project Folder Structure Overview

The project was structured to follow modular and scalable design principles, making each system feature independent and easy to maintain.

    banking-system/
    │
    ├── docs/
    │   ├── documentation/
    │   │   ├── D-01/
    │   │   │   └── day_01_documentation.md
    │   │   ├── flowchart.md
    │   │   ├── project_overview.md
    │   │   ├── pseudocode.md
    │   │   ├── sample_outputs.md
    │   │   ├── scope_&_limitations.md
    │   │   └── transaction_rules.md
    │   └── README.md
    │
    ├── features/
    │   ├── feature_login_auth/
    │   │   ├── login_authentication_feature.py
    │   │   ├── README.md
    │   │   └── __init__.py
    │   ├── feature_account_system/
    │   ├── feature_balance_inquiry/
    │   ├── feature_deposit/
    │   ├── feature_transaction_menu/
    │   ├── feature_transfer_funds/
    │   ├── feature_withdrawal/
    │   └── __init__.py
    │
    ├── utils/
    │   ├── terminal_ui.py
    │   └── __init__.py
    │
    └── testing/

### 🔐 Implemented Feature: Login Authentication

1. 📌 Feature Description

The Login Authentication feature allows the system to validate user credentials before granting access to the banking system.

2. ✔️ Functionalities Implemented

I. Accepts username and password input
II. Limits login attempts to prevent brute-force access
III. Displays a centered terminal UI using utility functions
IV. Shows appropriate messages for:

- Successful login
- Invalid credentials
- Maximum attempts reached

3. 🧩 Feature Location
features/feature_login_auth/
└── login_authentication_feature.py

4. 🛠️ Utilities Used

- terminal_ui.py

Located in:

- utils/terminal_ui.py

This utility file handles:

- Text centering based on terminal width
- Banner display
- Consistent console UI formatting

This keeps UI logic separate from system logic, improving readability and reusability.

### 🧠 Design Approach

I. Modular architecture: 
 
 - Each feature has its own folder

II. Separation of concerns:
 
 - UI handled in utils
 - Features handled in features

III. Scalable structure: 
 
 - New banking features can be added without breaking existing ones

### 🚀 Current System Status

✔ Project structure finalized
✔ Login Authentication feature implemented
✔ Terminal UI utilities created
✔ Documentation initialized

### 🔜 Next Planned Features

- Account creation system
- Balance inquiry
- Transaction menu
- Deposit and withdrawal features

### 📝 Notes

This documentation will be expanded daily to reflect newly implemented features and system improvements.
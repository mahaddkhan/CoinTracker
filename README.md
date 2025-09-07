# CoinTracker: Cryptocurrency Portfolio Tracker

![Python](https://img.shields.io/badge/Python-3.11-blue)
![GitHub Repo](https://img.shields.io/badge/GitHub-CoinTracker-orange)

---

## Description
CoinTracker is a Python-based cryptocurrency portfolio tracker that lets users securely manage their crypto holdings and track investments from the command line. The application uses the CoinGecko API to fetch real-time cryptocurrency prices and provides features like wallet management, profit/loss tracking, and secure coin removal. Its modular, class-based design keeps the project organized and easy to expand.

---

## Features

- 🔒 **User Authentication:** Sign up and log in securely with username, email, password, and 4-digit PIN.
- 💰 **Wallet Management:** View, add, and remove coins. Real-time prices fetched automatically.
- 🛡️ **Secure Coin Removal:** Removing a coin requires the correct PIN.
- 📊 **Profit & Loss Calculation:** Shows total money spent, current value, profit/loss, and percentage change.
- 🎨 **Color-Coded Output:** Green = profit, red = loss, yellow = money spent.
- ⚡ **Robust API Handling:** Gracefully handles missing coin data or temporary API errors.

---

## File & Folder Structure

```
crypto_tracker/
├── crypto_tracker/
│ ├── __init__.py
│ ├── main.py # Entry point for the application
│ ├── user.py # User signup, login, and authentication
│ ├── wallet.py # Wallet-related actions: view, add, remove, balance
│ ├── coin.py # Coin data fetching and API integration
│ └── utils.py # Utility functions (generate transaction ID, file checks)
├── users.csv # Stores user data: username, email, password hash, PIN hash
├── wallets.csv # Stores wallet transactions: coin, amount, price, tx_id
├── requirements.txt # Required Python packages
└── README.md
```
---

## How to Use

### Getting Started
1. Make sure you have **Python 3.11+** installed.
2. Install required packages:
```bash
pip install -r requirements.txt
```
3. Run the main script
```bash
python crypto_tracker/main.py
```

### Using CoinTracker
1. Sign up for an account or log in with an existing email and password.
2. Use the crypto menu to:
   - View your wallet  
   - Add coins  
   - Remove coins (requires PIN)  
   - Check portfolio balance and profit/loss
3. All wallet and user data is saved in `wallets.csv` and `users.csv`, so your portfolio persists across sessions.

---

## Design Decisions

1. **Modular Structure:**  
   The project is divided into separate modules (`user.py`, `wallet.py`, `coin.py`, `utils.py`) to keep the code organized, reusable, and easier to maintain.

2. **File-Based Storage:**  
   User and wallet data are stored in CSV files instead of a database, keeping the project lightweight and simple.

3. **Command-Line Interface (CLI):**  
   A CLI was chosen for simplicity and cross-platform compatibility. It allows the project to run without extra dependencies like GUI frameworks.

4. **Security:**  
   Passwords and PINs are hashed using SHA-256 before storage, giving basic protection for user credentials.

5. **Error Handling:**  
   Invalid inputs, missing coins, or API failures are handled gracefully, providing user-friendly messages instead of crashing the program.

---

## Conclusion

CoinTracker is a beginner-friendly yet robust project that demonstrates file-based data management, secure authentication, API integration, and real-time cryptocurrency portfolio tracking. Its modular and class-based design makes it easy to expand and maintain.
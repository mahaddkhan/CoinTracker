# CoinTracker: Cryptocurrency Portfolio Tracker

#### Description:
CoinTracker is a Python-based cryptocurrency portfolio tracker that lets users securely manage their crypto holdings and track investments from the command line. The application uses the CoinGecko API to fetch real-time cryptocurrency prices and provides features like wallet management, profit and loss tracking, and secure coin removal. Its modular design and class-based structure make the project organized and easy to expand.

---

## Features

- **User Authentication:**  
  Users can sign up with a unique username, email, password, and a 4-digit PIN. Login ensures that only authorized users can access their wallets.

- **Wallet Management:**  
  Users can view their wallet with all owned coins, amounts, and original prices. Adding coins automatically fetches real-time prices for accurate tracking.

- **Secure Coin Removal:**  
  Removing a coin requires the correct PIN, protecting users from accidental deletions or unauthorized access.

- **Profit & Loss Calculation:**  
  CoinTracker calculates total money spent, current portfolio value, profit/loss, and percentage change, giving users a clear picture of their investments.

- **Color-Coded Output:**  
  Financial values are color-coded for easy visual interpretation: green for profit, red for loss, and yellow for money spent.

- **Robust API Handling:**  
  Temporary API errors or missing coin data are handled gracefully, preventing program crashes.

---

## File & Folder Structure
```
crypto_tracker/
├── crypto_tracker/
│   ├── __init__.py
│   ├── main.py        # Entry point for the application
│   ├── user.py        # User signup, login, and authentication
│   ├── wallet.py      # Wallet-related actions: view, add, remove, balance
│   ├── coin.py        # Coin data fetching and API integration
│   └── utils.py       # Utility functions (generate transaction ID, file checks)
├── users.csv          # Stores user data: username, email, password hash, PIN hash
├── wallets.csv        # Stores wallet transactions: coin, amount, price, tx_id
├── requirements.txt   # Required Python packages
└── README.md
```
---

## How to Use

1. Run the `main.py` script in a Python 3.11+ environment.
2. Sign up for an account or log in with an existing email and password.
3. Use the crypto menu to:
   - View your wallet  
   - Add coins  
   - Remove coins (requires PIN)  
   - Check portfolio balance and profit/loss
4. All wallet and user data is saved in `wallets.csv` and `users.csv`, so your portfolio persists across sessions.

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
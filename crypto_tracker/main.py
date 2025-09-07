import sys
from crypto_tracker.user import signup, login
from crypto_tracker.wallet import view_wallet, add_coin, remove_coin, check_balance
from crypto_tracker.utils import ensure_users_file, ensure_wallets_file

USER_FILE = "users.csv"
WALLET_FILE = "wallets.csv"

def main():
    while True:
        print("\nMain Menu:")
        print("1. Sign up")
        print("2. Log in")
        print("3. Exit")
        choice = input("> ").strip()
        
        if choice == "1":
            username = signup(USER_FILE)
            if username:
                crypto_menu(username)
        elif choice == "2":
            username = login(USER_FILE)
            if username:
                crypto_menu(username)
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice")

def crypto_menu(username):
    while True:
        print(f"\n=== Crypto Menu ({username}) ===")
        print("1. View Wallet")
        print("2. Add Coin")
        print("3. Remove Coin (PIN required)")
        print("4. Check Balance & Profit %")
        print("5. Log out")
        choice = input("> ").strip()

        if choice == "1":
            view_wallet(username, WALLET_FILE)
        elif choice == "2":
            add_coin(username, WALLET_FILE)
        elif choice == "3":
            remove_coin(username, WALLET_FILE, USER_FILE)
        elif choice == "4":
            check_balance(username, WALLET_FILE)
        elif choice == "5":
            print(f"Logging out {username}...\n")
            return

if __name__ == "__main__":
    main()

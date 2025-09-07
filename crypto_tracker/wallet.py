import os
import csv
import hashlib
import time
from tabulate import tabulate
from crypto_tracker.utils import generate_tx_id, ensure_wallets_file
from crypto_tracker.coin import fetch_coin
from crypto_tracker.utils import WALLET_FILE


def view_wallet(username, wallet_file):
    ensure_wallets_file(WALLET_FILE)
    with open(wallet_file, "r") as file:
        reader = csv.DictReader(file)
        rows = [row for row in reader if row["username"] == username]

    if not rows:
        print("\n📭 Your wallet is empty.")
        input("\nPress Enter to return to the menu...")
        return

    table = [[row["tx_id"], row["coin"], row["amount"], f"${float(row['price_when_added']):,.2f}"] for row in rows]
    headers = ["Transaction ID", "Coin", "Amount", "Price When Added (USD)"]
    print("\n📊 Your Wallet:")
    print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
    input("\nPress Enter to return to the menu...")


def add_coin(username, wallet_file):
    ensure_wallets_file(WALLET_FILE)

    coin_id = input("Enter coin ID (e.g., bitcoin, ethereum): ").strip().lower()
    coin_data = fetch_coin(coin_id)
    if not coin_data:
        print("❌ Coin not found. Please try again.")
        return
    
    try:
        price_usd = coin_data["market_data"]["current_price"]["usd"]
    except KeyError:
        print("❌ Could not retrieve price for this coin.")
        return

    while True:
        try:
            amount = float(input(f"Enter amount of {coin_id} to add: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    tx_id = generate_tx_id()

    with open(wallet_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, coin_id, amount, price_usd, tx_id])

    print(f"✅ Added {amount} {coin_id} at ${price_usd:.2f} each to your wallet. (ID: {tx_id})")


def remove_coin(username, wallet_file, user_file):
    ensure_wallets_file(WALLET_FILE)

    log_in = False

    attempt_count = 0
    while attempt_count < 3:
        pin = input("Enter PIN: ")
        pin_hash = hashlib.sha256(pin.encode()).hexdigest()

        with open(user_file, "r") as file:
            reader = csv.DictReader(file)
            valid = False
            for row in reader:
                if row["username"] == username and row["pin_hash"] == pin_hash:
                    valid = True
                    break

        if valid:
            break
        else:
            attempt_count += 1
            print("Incorrect PIN")

    if attempt_count == 3:
        print("Too many incorrect attempts. Returning to menu.")
        return
                    
    print("\nEnter Transaction ID: (eg. 8ZSFTE, T6HT7A)")
    tx_id = input("> ").strip()

    with open(wallet_file, "r", newline='') as file, open("temp_wallets.csv", "w", newline='') as temp:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(temp, fieldnames=fieldnames)
        writer.writeheader()

        removed = False
        for row in reader:
            if row["tx_id"] == tx_id and row["username"] == username:
                removed = True
                continue
            writer.writerow(row)

    if not removed:
        print("Transaction ID not found for this user.")
        os.remove("temp_wallets.csv")
        return

    os.remove(wallet_file)
    os.rename("temp_wallets.csv", wallet_file)
    print("✅ Transaction removed successfully.")

    

def check_balance(username, wallet_file):
    ensure_wallets_file(WALLET_FILE)

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    money_spent = 0.0
    current_balance = 0.0


    with open(wallet_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username:
                money_spent = float(row["price_when_added"]) + money_spent

                coin_data = fetch_coin(row["coin"])
                time.sleep(0.2)
                if coin_data is None:
                    print(f"⚠️ Could not fetch data for {row['coin']}, skipping...")
                    continue 

                current_balance = current_balance + int(coin_data["market_data"]["current_price"]["usd"])
    
    total_profit = current_balance - money_spent
    percentage_profit = ((current_balance - money_spent) / money_spent) * 100

    print(f"\nMoney spent: {YELLOW}${money_spent:.0f}{RESET}")
    print(f"Profit achieved: {GREEN if total_profit >= 0 else RED}${total_profit:.0f}{RESET}")
    print(f"Total Increase / Decrease in value: {GREEN if percentage_profit >= 0 else RED}{percentage_profit:.2f}%{RESET}")
    input("\nPress Enter to return to the menu...")


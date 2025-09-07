import os
import random
import string
import csv

WALLET_FILE = "wallets.csv"

def generate_tx_id(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def ensure_users_file(user_file):
    if not os.path.exists(user_file):
        with open(user_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "email", "password_hash", "pin_hash"])

def ensure_wallets_file(wallet_file):
    if not os.path.exists(wallet_file):
        with open(wallet_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "coin", "amount", "price_when_added", "tx_id"])
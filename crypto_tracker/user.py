import csv
import hashlib
import re
from crypto_tracker.utils import ensure_users_file

def signup(user_file):
    ensure_users_file(user_file)
    print("\n(Enter 'q' at any time to return to Main Menu)")

    while True:
        username = input("\nChoose a Username: ").strip()
        if username.lower() == "q":
            return None
        if not username:
            print("Username cannot be empty.")
            continue

        with open(user_file, "r") as file:
            reader = csv.DictReader(file)
            if any(row["username"].lower() == username.lower() for row in reader):
                print("Username already taken. Please choose another.")
                continue
        break

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    while True:
        email = input("\nCreate Email: ").strip().lower()
        if email.lower() == "q":
            return None
        if not re.match(pattern, email):
            print("Invalid email format. Try again.")
            continue

        with open(user_file, "r") as file:
            reader = csv.DictReader(file)
            if any(row["email"] == email for row in reader):
                print("Email already registered. Please log in instead.")
                return None
        break

    while True:
        password = input("Password: ").strip()
        if password.lower() == "q":
            return None
        password2 = input("Confirm Password: ").strip()
        if password2.lower() == "q":
            return None
        if password != password2:
            print("Passwords do not match. Try again.")
            continue
        break

    while True:
        pin = input("Create 4-digit PIN: ").strip()
        if pin.lower() == "q":
            return None
        pin2 = input("Confirm PIN: ").strip()
        if pin2.lower() == "q":
            return None
        if pin != pin2 or not pin.isdigit() or len(pin) != 4:
            print("PIN must be 4 digits and match. Try again.")
            continue
        break

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    pin_hash = hashlib.sha256(pin.encode()).hexdigest()

    with open(user_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, email, password_hash, pin_hash])

    print("\nAccount created successfully. Proceed to login.")
    return username

def login(user_file):
    ensure_users_file(user_file)
    for attempt in range(3):
        email = input("\nEmail: ").strip().lower()
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        if not re.match(pattern, email):
            if attempt == 2:
                print("\nToo many failed attempts. Please try logging in again.")
                return None
            else:
                print("Invalid email format. Try again.")
        else:
            break
    
    with open(user_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["email"] == email:
                for _ in range(3):
                    password = input("Password: ").strip()
                    password_hash = hashlib.sha256(password.encode()).hexdigest()
                    if row["password_hash"] == password_hash:
                        print("Login successful!")
                        return row["username"]
                    else:
                        print(f"Incorrect password.")
                print("\nToo many failed attempts. Please try logging in again.")
                return None
        print("Email not found. Please sign up first.")
        return None
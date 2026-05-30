# --- Imports ---
import json
import os

# --- Configuration / storage paths ---
# The folder where this script lives, so data files are loaded relative to it.
BASE_DIR = os.path.dirname(__file__)
# The data directory inside the script folder.
DATA_DIR = os.path.join(BASE_DIR, "data")
# The JSON file path where account data is saved and loaded.
ACCOUNTS_FILE = os.path.join(DATA_DIR, "accounts.json")

print("DIGI-WALLET")

# --- Default accounts used when the data file does not exist ---
DEFAULT_ACCOUNTS = {
    "John Account": {"password": "pass1", "balance": 100.0},
    "Jane Account": {"password": "pass2", "balance": 0.0},
}

# --- File storage helpers ---

def ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def load_accounts():
    ensure_data_dir()
    if not os.path.exists(ACCOUNTS_FILE):
        save_accounts(DEFAULT_ACCOUNTS)
        return DEFAULT_ACCOUNTS.copy()

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as handle:
            data = json.load(handle)
            if isinstance(data, dict):
                return data
    except (json.JSONDecodeError, OSError):
        pass

    return DEFAULT_ACCOUNTS.copy()


def save_accounts(accounts):
    ensure_data_dir()
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as handle:
        json.dump(accounts, handle, indent=2)


accounts = load_accounts()

# --- Utility helpers ---

def get_positive_amount(prompt):
    try:
        amount = float(input(prompt).strip())
        if amount <= 0:
            print("Amount must be greater than zero.")
            return None
        return amount
    except ValueError:
        print("Please enter a valid number.")
        return None

# --- Authentication: login and registration ---


def login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    user = accounts.get(username)

    if user and user.get("password") == password:
        print("Login successful. Welcome to Digi-Wallet!")
        account_menu(username)
    else:
        print("Invalid credentials. Try again.")


def register():
    username = input("Choose a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return
    if username in accounts:
        print("Username already exists. Try again.")
        return

    password = input("Choose a password: ").strip()
    if not password:
        print("Password cannot be empty.")
        return

    accounts[username] = {"password": password, "balance": 0.0}
    save_accounts(accounts)
    print("Registration successful. You can now log in.")

# --- Account actions after login ---

def account_menu(username):
    while True:
        print(f"Hello, {username}!")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Choose 1-4: ").strip()

        if choice == "1":
            balance = accounts[username].get("balance", 0.0)
            print(f"\nYour balance is: ${balance:.2f}\n")
        elif choice == "2":
            amount = get_positive_amount("Enter deposit amount: ")
            if amount is not None:
                accounts[username]["balance"] += amount
                save_accounts(accounts)
                print(f"\nDeposited ${amount:.2f}. New balance: ${accounts[username]['balance']:.2f}\n")
        elif choice == "3":
            amount = get_positive_amount("Enter withdrawal amount: ")
            if amount is not None:
                balance = accounts[username].get("balance", 0.0)
                if amount > balance:
                    print("Insufficient funds.")
                else:
                    accounts[username]["balance"] -= amount
                    save_accounts(accounts)
                    print(f"\nWithdrawn ${amount:.2f}. New balance: ${accounts[username]['balance']:.2f}\n")
        elif choice == "4":
            print("Logged out.")
            break
        else:
            print("Please choose a valid option.")

# --- Main menu ---

def main():
    while True:
        print("Choose an option:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter 1, 2 or 3: ").strip()

        if choice == "1":
            login()
        elif choice == "2":
            register()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2 or 3.")


# --- starting point ---
if __name__ == "__main__":
    main()

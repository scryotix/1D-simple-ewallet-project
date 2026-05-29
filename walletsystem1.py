# testing 1
logindata = {
    "user1": "pass1",
    "user2": "pass2"
}

print("DIGI-WALLET")

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in logindata and logindata[username] == password:
        print("Login successful. Welcome to Digi-Wallet!")
    else:
        print("Invalid credentials. Try again.")
def register():
    username = input("Choose a username: ")
    if username in logindata:
        print("Username already exists. Try again.")
    else:
        password = input("Choose a password: ")
        logindata[username] = password
        print("Registration successful. You can now log in.")


def main():
    while True:
        print("\nChoose an option:")
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


if __name__ == "__main__":
    main()
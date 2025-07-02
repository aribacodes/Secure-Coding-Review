#  Vulnerable User System: Register + Login (Educational Purpose Only)

# WARNING: This script contains intentional security flaws to be reviewed and fixed.

def register_user():
    print(" Register New User")
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    #  Insecure: Storing password as plain text
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
    print("User registered successfully!")

def login_user():
    print(" User Login")
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as f:
            users = f.readlines()

        #  Insecure: Direct comparison of plain text
        for user in users:
            stored_user, stored_pass = user.strip().split(",")
            if username == stored_user and password == stored_pass:
                print("Login successful!")
                return
        print("Invalid credentials.")
    except FileNotFoundError:
        print("No users found. Please register first.")

def main():
    print("=== Welcome to SecureCorp ===")
    print("1. Register")
    print("2. Login")
    choice = input("Select an option (1 or 2): ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()

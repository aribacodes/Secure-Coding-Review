import bcrypt
import os

USERS_FILE = "users.txt"

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def is_valid_input(input_str):
    return input_str and input_str.strip() != ""

def user_exists(username):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "rb") as f:
        for line in f:
            stored_user, _ = line.strip().split(b",")
            if stored_user.decode() == username:
                return True
    return False

def register_user():
    print(" Register New User")
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()

    if not is_valid_input(username) or not is_valid_input(password):
        print(" Invalid input. Please enter non-empty values.")
        return

    if user_exists(username):
        print(" Username already exists. Please choose another one.")
        return

    hashed_pw = hash_password(password)
    with open(USERS_FILE, "ab") as f:
        f.write(username.encode() + b"," + hashed_pw + b"\n")
    print(" User registered successfully!")

def login_user():
    print(" User Login")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if not is_valid_input(username) or not is_valid_input(password):
        print("❌ Invalid input.")
        return

    try:
        with open(USERS_FILE, "rb") as f:
            users = f.readlines()

        for user in users:
            stored_user, stored_hashed = user.strip().split(b",")
            if stored_user.decode() == username and check_password(password, stored_hashed):
                print(" Login successful!")
                return
        print(" Invalid credentials.")
    except Exception as e:
        print(f" An error occurred: {e}")

def main():
    print("=== Welcome to SecureCorp ===")
    print("1. Register")
    print("2. Login")
    choice = input("Select an option (1 or 2): ").strip()

    if choice == "1":
        register_user()
    elif choice == "2":
        login_user()
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
2

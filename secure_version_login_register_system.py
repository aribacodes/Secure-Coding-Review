import bcrypt
import os

# File to store user credentials
USERS_FILE = "users.txt"

# Separator used to safely distinguish between username and hashed password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Function to verify a plain password against its hashed version
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
    
# Function to ensure input is not empty or just whitespace
def is_valid_input(input_str):
    return input_str and input_str.strip() != ""

# Function to check if a username already exists in the file
def user_exists(username):
    if not os.path.exists(USERS_FILE):
        return False
    with open(USERS_FILE, "rb") as f:
        for line in f:
             # Splitting the stored username and hashed password
            stored_user, _ = line.strip().split(b",")
            if stored_user.decode() == username:
                return True
    return False
# Function to handle new user registration
def register_user():
    print(" Register New User")
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()
# Check for valid (non-empty) inputs
    if not is_valid_input(username) or not is_valid_input(password):
        print(" Invalid input. Please enter non-empty values.")
        return
        # Prevent duplicate usernames
    if user_exists(username):
        print(" Username already exists. Please choose another one.")
        return
# Hash the password and store it with the username
    hashed_pw = hash_password(password)
    with open(USERS_FILE, "ab") as f:
        f.write(username.encode() + b"," + hashed_pw + b"\n")
    print(" User registered successfully!")
# Function to handle user login
def login_user():
    print(" User Login")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
# Check for valid (non-empty) inputs
    if not is_valid_input(username) or not is_valid_input(password):
        print("Invalid input.")
        return
    try:
        # Open the user file and read all lines
        with open(USERS_FILE, "rb") as f:
            users = f.readlines()
            
# Loop through each user entry to verify credentials
        for user in users:
            stored_user, stored_hashed = user.strip().split(b",")
            if stored_user.decode() == username and check_password(password, stored_hashed):
                print(" Login successful!")
                return
        print(" Invalid credentials.")     # If no match found
    except Exception as e:
        print(f" An error occurred: {e}")   # Handles unexpected errors like file format issues

# Main function: Displays menu and handles user's choice
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

# Program starts here
if __name__ == "__main__":
    main()


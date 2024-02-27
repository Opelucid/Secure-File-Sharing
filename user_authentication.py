# user_authentication.py
from getpass import getpass
import hashlib
from config import USERNAME, PASSWORD

def authenticate():
    print("User Authentication")
    
    # Get user input
    username_input = input("Enter your username: ")
    password_input = getpass("Enter your password: ")

    # Hash the password input
    hashed_password_input = hash_password(password_input)

    # Check if the provided username and hashed password match the configured values
    return username_input == USERNAME and hashed_password_input == PASSWORD

def hash_password(password):
    # Hash the password using SHA256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

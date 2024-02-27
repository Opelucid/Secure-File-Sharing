import numpy as np
import math
import secrets
import user_authentication
import encryption
import file_handling

def main():
    print("Secure File Sharing System:")

    # Authenticate user
    if user_authentication.authenticate():
        print("Authentication successful.")
        option = input("Choose an option (1. Encrypt File, 2. Decrypt File): ")

        if option == "1":
            file_handling.encrypt_file()
        elif option == "2":
            file_handling.decrypt_file()
        else:
            print("Invalid option. Exiting.")

    else:
        print("Authentication failed. Exiting.")

if __name__ == "__main__":
    main()

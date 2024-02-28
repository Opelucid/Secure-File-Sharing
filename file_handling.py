import os
import encryption
from config import ENCRYPTED_FILES_DIR, DECRYPTED_FILES_DIR

def encrypt_file():
    # take file path from user
    file_path = input("Enter the path of the file to encrypt: ")

    # Check if the file exists
    if not os.path.isfile(file_path):
        print("File not found. Exiting.")
        return

    # Read the content of the file
    with open(file_path, 'rb') as file:
        file_content = file.read()

    # Encrypt the file content
    encrypted_content = encryption.encrypt(file_content)

    # Get the file name (excluding the path)
    file_name = os.path.basename(file_path)

    # Save the encrypted content to a new file
    encrypted_file_path = os.path.join(ENCRYPTED_FILES_DIR, f"encrypted_{file_name}")
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_content)

    print(f"File encrypted successfully. Encrypted file saved at: {encrypted_file_path}")

def decrypt_file():
    # Get the file path from the user
    encrypted_file_path = input("Enter the path of the encrypted file to decrypt: ")

    # Check if the file exists 
    if not os.path.isfile(encrypted_file_path):
        print("Encrypted file not found. Exiting.")
        return

    # Read the content of the encrypted file
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_content = encrypted_file.read()

    # Decrypt the file content
    decrypted_content = encryption.decrypt(encrypted_content)

    # Get the original file name
    original_file_name = os.path.basename(encrypted_file_path).replace("encrypted_", "")

    # Save the decrypted content to a new file
    decrypted_file_path = os.path.join(DECRYPTED_FILES_DIR, f"decrypted_{original_file_name}")
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_content)

    print(f"File decrypted successfully. Decrypted file saved at: {decrypted_file_path}")

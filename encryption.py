#hi :d
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding, hashes
import os
from config import SYMMETRIC_ALGORITHM, ASYMMETRIC_ALGORITHM

def generate_symmetric_key():
    return os.urandom(32)

def encrypt(data):
    if SYMMETRIC_ALGORITHM == "AES":
        key = generate_symmetric_key()
        cipher = Cipher(algorithms.AES(key), modes.CFB(), backend=default_backend())

    encryptor = cipher.encryptor()
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()
    return key + encryptor.update(padded_data) + encryptor.finalize()

def decrypt(data):
    # maybe switch algo to something else not sure tbh
    if SYMMETRIC_ALGORITHM == "AES":
        key = data[:32]
        cipher = Cipher(algorithms.AES(key), modes.CFB(), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = decryptor.update(data[32:]) + decryptor.finalize()

    return unpadder.update(decrypted_data) + unpadder.finalize()

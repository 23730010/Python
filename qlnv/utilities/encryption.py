# pip install cryptography

from cryptography.fernet import Fernet


class Encryption:
    def __init__(self):
        self.__key_file_path = "./resources/secret.key"
        self.__key = self.load_key()

    # Generate and save a key (do this once and store the key securely)
    def generate_key(self):
        """Generate key"""
        key = Fernet.generate_key()
        with open(self.__key_file_path, "wb") as key_file:
            key_file.write(key)

    # Load the key
    def load_key(self):
        """load the key for encryption"""
        with open(self.__key_file_path, "rb") as key_file:
            return key_file.read()

    # Encode (encrypt) the password
    def encode_password(self, password):
        """encode password"""
        fernet = Fernet(self.__key)
        encoded_password = fernet.encrypt(password.encode())
        return encoded_password

    # Decode (decrypt) the password
    def decode_password(self, encoded_password):
        """decode password"""
        fernet = Fernet(self.__key)
        decoded_password = fernet.decrypt(encoded_password).decode()
        return decoded_password

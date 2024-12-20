# pip install cryptography

from cryptography.fernet import Fernet


class Encryption:
    def __init__(self):
        self.__key_file_path = "./resources/secret.key"
        self.__key = self.load_key()

    # Generate and save a key (do this once and store the key securely)
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.__key_file_path, "wb") as key_file:
            key_file.write(key)

    # Load the key
    def load_key(self):
        with open(self.__key_file_path, "rb") as key_file:
            return key_file.read()

    # Encode (encrypt) the password
    def encode_password(self, password):
        fernet = Fernet(self.__key)
        encoded_password = fernet.encrypt(password.encode())
        return encoded_password

    # Decode (decrypt) the password
    def decode_password(self, encoded_password):
        fernet = Fernet(self.__key)
        decoded_password = fernet.decrypt(encoded_password).decode()
        return decoded_password


# Main workflow
if __name__ == "__main__":
    ecryption = Encryption()

    # Password to encode
    original_password = "my_secure_password123"

    # Encoding the password
    encrypted_password = ecryption.encode_password(original_password)
    print(f"Encoded Password: {encrypted_password}")

    # Decoding the password
    decrypted_password = ecryption.decode_password(encrypted_password)
    print(f"Decoded Password: {decrypted_password}")

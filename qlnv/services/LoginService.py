from qlnv.repositories.UserRepository import UserRepository
from qlnv.utilities.encryption import Encryption


class LoginService:
    def __init__(self):
        self.__user_repo = UserRepository()
        self.__encryption = Encryption()

    def find_user_by_username(self, username):
        return self.__user_repo.find_user_by_username(username)

    def insert_user(self, user):
        self.__user_repo.insert_user(user)

    def compare_password_and_encoded_password(self, password, encrypt_password):
        password_temp = self.__encryption.decode_password(encrypt_password)
        return password_temp == password

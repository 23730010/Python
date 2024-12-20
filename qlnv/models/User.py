from qlnv.repositories.UserRepository import UserRepository
from qlnv.utilities.encryption import Encryption


class User:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__user_repo = UserRepository()

    @property
    def get_user_name(self):
        return str(self.__username)

    @property
    def get_encrypt_password(self):
        encrypt = Encryption()
        return encrypt.encode_password(self.__password)

    @property
    def get_password(self):
        return str(self.__password)

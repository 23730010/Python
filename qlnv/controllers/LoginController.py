from qlnv.controllers.QLNVController import QLNVController
from qlnv.models.User import User
from qlnv.services.LoginService import LoginService
from qlnv.views.LoginView import LoginView
from qlnv.views.RegisterView import RegisterView


class LoginController:
    def __init__(self):
        self.__user = None
        self.__login_screen = None
        self.__register_screen = None
        self._login_service = LoginService()

    def start(self):
        """Start login feature"""
        self.__user = None
        login_main = LoginController()
        login_main.open_login_screen(login_main)

    def open_login_screen(self, event):
        """Open the login screen"""
        self.__login_screen = LoginView(self)
        self.__login_screen.mainloop()

    def back_login_screen(self, event):
        """Back to the login screen from the register screen"""
        self.__register_screen.destroy()
        self.__login_screen = LoginView(self)
        self.__login_screen.mainloop()

    def open_register_screen(self, event):
        """Open register screen"""
        self.__login_screen.destroy()
        self.__register_screen = RegisterView(self)
        self.__register_screen.mainloop()

    def login(self, username, password):
        """Login and redirect to the QLNV screen"""
        user = self._login_service.find_user_by_username(username)

        if user is not None and self._login_service.compare_password_and_encoded_password(password, user.password):

            self.__login_screen.destroy()
            qlnv_controller = QLNVController(self, User(user.username, None))
            qlnv_controller.start()
        else:
            return 0

    def register(self, username, password):
        """Perform registering new user"""
        user = self._login_service.find_user_by_username(username)

        if user is None:
            new_user = User(username, password)
            return self._login_service.insert_user(new_user)
        else:
            return 2

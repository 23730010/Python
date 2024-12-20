import tkinter as tk
from tkinter import messagebox


class LoginView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller
        self.title("Đăng nhập")
        self.geometry("400x300")

        # Tiêu đề
        tk.Label(self, text="Màn hình Đăng nhập", font=("Arial", 16)).pack(pady=20)

        # Tên đăng nhập
        tk.Label(self, text="Tên đăng nhập:").pack(anchor="w", padx=20)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(pady=5, padx=20)

        # Mật khẩu
        tk.Label(self, text="Mật khẩu:").pack(anchor="w", padx=20)
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.pack(pady=5, padx=20)

        # Nút đăng nhập
        tk.Button(self, text="Đăng nhập", command=self.login).pack(pady=10)

        # Liên kết đến màn hình đăng ký
        register_link = tk.Label(
            self, text="Chưa có tài khoản? Đăng ký ngay!", fg="blue", cursor="hand2"
        )
        register_link.pack(pady=10)
        register_link.bind("<Button-1>", self.__controller.open_register_screen)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            result = self.__controller.login(username, password)
            if result == 0:
                messagebox.showerror("Thông báo", "Sai tên đăng nhập hoặc mật khẩu!")
        else:
            messagebox.showerror("Thông báo", "Sai tên đăng nhập hoặc mật khẩu!")

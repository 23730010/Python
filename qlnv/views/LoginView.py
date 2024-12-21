import tkinter as tk
from tkinter import messagebox

from qlnv.utilities.NVCommon import NVCommon


class LoginView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

        self.render_ui()

    def render_ui(self):
        self.title("Đăng nhập")
        self.geometry("400x300")

        NVCommon.show_center_of_window(self)

        # Tiêu đề
        tk.Label(self, text="Màn hình Đăng nhập", font=("Arial", 16)).pack(pady=20)

        # Tên đăng nhập
        username_frame = tk.Frame(self)
        username_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(username_frame, text="Tên đăng nhập:", width=15, anchor="w").grid(row=0, column=0, sticky="w")
        self.username_entry = tk.Entry(username_frame, width=30)
        self.username_entry.grid(row=0, column=1, padx=5)

        # Mật khẩu
        password_frame = tk.Frame(self)
        password_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(password_frame, text="Mật khẩu:", width=15, anchor="w").grid(row=0, column=0, sticky="w")
        self.password_entry = tk.Entry(password_frame, width=30, show="*")
        self.password_entry.grid(row=0, column=1, padx=5)

        # Nút đăng nhập
        tk.Button(self, text="Đăng nhập", width=15, command=self.login).pack(pady=10)

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
                messagebox.showerror("Thông báo", "Sai tên đăng nhập hoặc mật khẩu!", parent=self)
        else:
            messagebox.showerror("Thông báo", "Vui lòng nhập đầy đủ thông tin đăng nhập!", parent=self)

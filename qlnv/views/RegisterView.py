import tkinter as tk
from tkinter import messagebox


class RegisterView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller
        self.title("Đăng ký")
        self.geometry("400x400")

        # Tiêu đề
        tk.Label(self, text="Màn hình Đăng ký", font=("Arial", 16)).pack(pady=20)

        # Tên đăng nhập
        tk.Label(self, text="Tên đăng nhập:").pack(anchor="w", padx=20)
        self.username_entry = tk.Entry(self, width=30)
        self.username_entry.pack(pady=5, padx=20)

        # Mật khẩu
        tk.Label(self, text="Mật khẩu:").pack(anchor="w", padx=20)
        self.password_entry = tk.Entry(self, width=30, show="*")
        self.password_entry.pack(pady=5, padx=20)

        # Nút đăng ký
        tk.Button(self, text="Đăng ký", command=self.register).pack(pady=10)

        # Liên kết quay lại màn hình đăng nhập
        back_link = tk.Label(
            self, text="Quay lại đăng nhập", fg="blue", cursor="hand2"
        )
        back_link.pack(pady=10)
        back_link.bind("<Button-1>", self.__controller.back_login_screen)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            result = self.__controller.register(username, password)
            if result == 0:
                messagebox.showerror("Thông báo", "Đăng ký thất bại, vui lòng kiểm tra lại thông tin!")
            else:
                messagebox.showinfo("Thông báo", "Đăng ký thành công!")
                self.__controller.back_login_screen(self)
        else:
            messagebox.showerror("Thông báo", "Vui lòng nhập đầy đủ thông tin!")

import tkinter as tk
from tkinter import messagebox

from qlnv.utilities.NVCommon import NVCommon


class RegisterView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller

        self.render_ui()

    def render_ui(self):
        """Render UI of register screen"""
        self.title("Đăng ký")
        self.geometry("400x230")

        NVCommon.show_center_of_window(self)

        # Tiêu đề
        tk.Label(self, text="Màn hình Đăng ký", font=("Arial", 16)).pack(pady=20)

        # Tên đăng nhập
        username_frame = tk.Frame(self)
        username_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(username_frame, text=" *", fg="red").grid(row=0, column=0, sticky="w")
        tk.Label(username_frame, text="Tên đăng nhập:", width=15, anchor="w").grid(row=0, column=1, sticky="w")
        self.username_entry = tk.Entry(username_frame, width=30)
        self.username_entry.grid(row=0, column=2, padx=5)

        # Mật khẩu
        password_frame = tk.Frame(self)
        password_frame.pack(anchor="w", padx=20, pady=5)
        tk.Label(password_frame, text=" *", fg="red").grid(row=0, column=0, sticky="w")
        tk.Label(password_frame, text="Mật khẩu:", width=15, anchor="w").grid(row=0, column=1, sticky="w")
        self.password_entry = tk.Entry(password_frame, width=30, show="*")
        self.password_entry.grid(row=0, column=2, padx=5)

        # Nút đăng ký
        tk.Button(self, text="Đăng ký", width=15, command=self.register).pack(pady=10)

        # Liên kết quay lại màn hình đăng nhập
        back_link = tk.Label(
            self, text="Quay lại đăng nhập", fg="blue", cursor="hand2"
        )
        back_link.pack(pady=10)
        back_link.bind("<Button-1>", self.__controller.back_login_screen)


    def register(self):
        """Perform registering and alert the result"""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username and password:
            result = self.__controller.register(username, password)
            if result == 0:
                messagebox.showerror("Thông báo", "Đăng ký thất bại, vui lòng kiểm tra lại thông tin!", parent=self)
            elif result == 2:
                messagebox.showerror("Thông báo", "Tên đăng nhập đã tồn tại!", parent=self)
            else:
                messagebox.showinfo("Thông báo", "Đăng ký thành công!")
                self.__controller.back_login_screen(self)
        else:
            messagebox.showerror("Thông báo", "Vui lòng nhập đầy đủ thông tin!", parent=self)

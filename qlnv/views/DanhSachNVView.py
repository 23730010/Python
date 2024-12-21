import tkinter as tk
from functools import partial
from tkinter import messagebox, ttk

from qlnv.models.NVBanHang import NVBanHang
from qlnv.models.NVVanPhong import NVVanPhong
from qlnv.utilities.NVCommon import NVCommon


class DanhSachNVView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller
        self.canvas = None
        self.__ds_lable_button = []
        self.__vcmd = (self.register(NVCommon.validate_number_input), '%d', '%P')  # Validation command

        self.render_ui()

    def render_ui(self):
        """Render UI of QLNV screen"""
        self.title("Danh Sách Nhân Viên")
        self.geometry("810x500")

        NVCommon.show_center_of_window(self)

        # Header Frame
        header_frame = tk.Frame(self, bg="#f0f0f0", height=50)
        header_frame.pack(fill=tk.X)

        # Company name label
        company_label = tk.Label(header_frame,text=self.__controller.get_ten_cty(),font=("Arial", 16, "bold"),bg="#f0f0f0",anchor="w")
        company_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Logout button
        logout_button = tk.Button(header_frame, text="Đăng Xuất", command=self.logout_button_click, bg="#d9534f", fg="white", font=("Arial", 10, "bold") )
        logout_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # username label
        username_label = tk.Label(header_frame, text=self.__controller.user.get_user_name.strip(), font=("Arial", 12), bg="#f0f0f0",anchor="w")
        username_label.pack(side=tk.RIGHT, padx=10, pady=10)

        # Search Frame
        search_frame = tk.Frame(self, bg="#ffffff")
        search_frame.pack(pady=10, padx=10, fill=tk.X)

        # Search fields
        tk.Label(search_frame, text="Mã NV:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.ma_nv_entry = ttk.Entry(search_frame, width=30)
        self.ma_nv_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(search_frame, text="Họ Tên:", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.ho_ten_entry = ttk.Entry(search_frame, width=30)
        self.ho_ten_entry.grid(row=0, column=3, padx=5, pady=5)

        # Search button
        search_button = ttk.Button(search_frame, text="Tìm kiếm", width=15, command=self.search_button_click)
        search_button.grid(row=0, column=4, padx=10, pady=10)

        # Employee list (placeholder)
        employee_list_frame = tk.Frame(self, bg="#f8f9fa", height= 30)
        employee_list_frame.pack(pady=10, padx=10,fill=tk.X)

        employee_label = tk.Label(employee_list_frame,text="Danh sách nhân viên sẽ hiển thị tại đây",bg="#f8f9fa",font=("Arial", 12),anchor="center")
        employee_label.pack(fill=tk.Y, expand=True)

        # Nút làm mới
        refresh_button = ttk.Button(employee_list_frame, text="Làm mới Grid", width=15, command=self.refresh_data_button_click)
        refresh_button.pack(pady=10, padx=10, side=tk.RIGHT)

        # Add button
        add_button = ttk.Button(employee_list_frame, text="Thêm nhân viên", width=15, command=self.show_add_popup)
        add_button.pack(pady=10, padx=10, side=tk.RIGHT)

        # Bind the window close event
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def show_nv_list(self, ds):
        """Show list of nv under grid, using canvas"""
        # Create a Canvas for the table
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Create table headers
        headers = ["Mã NV", "Họ Tên", "Lương CB", "Lương Ht", "Số sp", "Số ng", "Loại NV", "Sửa", "Xóa", "Tính Lương"]
        for col_index, header in enumerate(headers):
            width = 10
            if col_index == 1:
                width = 15

            tk.Label(self.canvas, text=header, relief=tk.RIDGE, width=width, bg="lightgray").grid(row=0,
                                                                                                  column=col_index)

        # Populate the table with data and buttons
        for row_index, row_data in enumerate(ds, start=1):
            self.add_row(row_index, row_data)


    def add_row(self, row_index, row_data):
        """Add nv to grid"""
        # Thêm từng ô dữ liệu vào Canvas
        label_ma_nv = tk.Label(self.canvas, text=row_data._ma_nv, relief=tk.RIDGE, width=10)
        label_ma_nv.grid(row=row_index, column=0)
        label_ho_ten = tk.Label(self.canvas, text=row_data._ho_ten, relief=tk.RIDGE, width=15)
        label_ho_ten.grid(row=row_index, column=1)
        label_luong_cb = tk.Label(self.canvas, text=int(float(str(row_data._luong_cb).strip())), relief=tk.RIDGE, width=10)
        label_luong_cb.grid(row=row_index, column=2)
        label_luong_ht = tk.Label(self.canvas, text=int(float(str(row_data._luong_ht).strip())) if row_data._luong_ht is not None else 'Chưa tính', relief=tk.RIDGE, width=10)
        label_luong_ht.grid(row=row_index, column=3)
        label_so_sp = tk.Label(self.canvas, text=row_data._so_sp if hasattr(row_data, '_so_sp') else None, relief=tk.RIDGE, width=10)
        label_so_sp.grid(row=row_index, column=4)
        label_so_ng = tk.Label(self.canvas, text=row_data._so_ng if hasattr(row_data, '_so_ng') else None, relief=tk.RIDGE, width=10)
        label_so_ng.grid(row=row_index, column=5)
        label_loai_nv = tk.Label(self.canvas,text=('NV Bán Hàng' if isinstance(row_data, NVBanHang) else 'NV Văn Phòng'), relief=tk.RIDGE, width=10)
        label_loai_nv.grid(row=row_index, column=6)
        bt_edit = tk.Button(self.canvas, text="Edit", command=lambda r=row_data: self.edit_button_click(r), width=8)
        bt_edit.grid(row=row_index, column=7)
        bt_delete = tk.Button(self.canvas, text="Delete", command=lambda r=row_data: self.delete_button_click(r), width=8)
        bt_delete.grid(row=row_index, column=8)

        if row_data._luong_ht == None:
            bt_tinh_luong = tk.Button(self.canvas, text="Tính lương", command=lambda r=row_data: self.button_calculate_salary(r), width=8)
            bt_tinh_luong.grid(row=row_index, column=9)
            self.__ds_lable_button.append(bt_tinh_luong)
        else:
            label_tinh_luong = tk.Label(self.canvas, text='Đã tính', relief=tk.RIDGE, width=9)
            label_tinh_luong.grid(row=row_index, column=9)
            self.__ds_lable_button.append(label_tinh_luong)

        self.__ds_lable_button.extend(
            [label_ma_nv, label_ho_ten, label_luong_cb, label_luong_ht, label_so_sp, label_so_ng, label_loai_nv,
             bt_edit, bt_delete])

    def logout_button_click(self):
        """Click event for logout button"""
        self.__controller.logout()

    def search_button_click(self):
        """Click event for search button"""
        ma_nv = self.ma_nv_entry.get().strip().lower()
        ho_ten = self.ho_ten_entry.get().strip().lower()
        self.refresh_data(self.__controller.search_nv(ma_nv, ho_ten))

    def edit_button_click(self, row):
        """click event for edit button"""
        self.show_edit_popup(row)

    def delete_button_click(self, row):
        """Click event for delete button"""
        self.__controller.delete_nv(row)
        self.refresh_data(self.__controller.refresh_data())

    def button_calculate_salary(self, nv):
        """Click event for calculate salary button"""
        self.__controller.tinh_luong(nv)
        self.refresh_data(self.__controller.refresh_data())

    def refresh_data_button_click(self):
        """Click event for refresh data button"""
        self.refresh_data(self.__controller.refresh_data())

    def close_window(self):
        """Close window"""
        self.destroy()  # This closes the window

    # Hàm giả lập tải dữ liệu mới
    def refresh_data(self, ds):
        """Refresh data on grid"""
        # Xóa các phần tử cũ trên Canvas
        self.delete_button_label()
        for row_index, row_data in enumerate(ds, start=1):
            self.add_row(row_index, row_data)

    def delete_button_label(self):
        """Delete buttons and labels on grid"""
        # Hủy tất cả các Label và button trên canvas
        for item in self.__ds_lable_button:
            item.destroy()
        self.__ds_lable_button.clear()

    # Function to show the popup for editing employee details
    def show_edit_popup(self, nv):
        """Show edit nv popup"""
        # Create a new window (popup) for editing information
        popup = tk.Toplevel(self)
        popup.title("Cập nhật thông tin nhân viên")
        popup.geometry("310x250")

        NVCommon.show_center_of_window(popup)

        # Variables to hold the data
        ma_nv = tk.StringVar(value=nv._ma_nv)
        ho_ten = tk.StringVar(value=nv._ho_ten)
        luong_cb = tk.StringVar(value=int(float(nv._luong_cb)))
        so_sp = None
        so_ng = None

        # Mã nhân viên
        tk.Label(popup, text="Mã NV:").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(popup, textvariable=ma_nv).grid(row=0, column=2, padx=5, pady=5)

        # Họ và tên
        tk.Label(popup, text=" *", fg="red").grid(row=1, column=0, sticky="e")
        tk.Label(popup, text="Họ và tên:").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ho_ten_entry = tk.Entry(popup, textvariable=ho_ten, width=30)
        ho_ten_entry.grid(row=1, column=2, padx=5, pady=5)

        # lương cơ bản
        tk.Label(popup, text=" *", fg="red").grid(row=2, column=0, sticky="e")
        tk.Label(popup, text="Lương cơ bản:").grid(row=2, column=1, padx=5, pady=5, sticky="w")
        luong_cb_entry = tk.Entry(popup, textvariable=luong_cb, validate="key", validatecommand=self.__vcmd, width=30)
        luong_cb_entry.grid(row=2, column=2, padx=5, pady=5)

        if isinstance(nv, NVBanHang):
            so_sp = tk.StringVar(value=int(float(nv._so_sp)))

            # Số sản phẩm
            tk.Label(popup, text=" *", fg="red").grid(row=3, column=0, sticky="e")
            tk.Label(popup, text="Số sản phẩm:").grid(row=3, column=1, padx=5, pady=5, sticky="w")
            so_sp_entry = tk.Entry(popup, textvariable=so_sp, validate="key", validatecommand=self.__vcmd, width=30)
            so_sp_entry.grid(row=3, column=2, padx=5, pady=5)
        else:
            so_ng = tk.StringVar(value=int(float(nv._so_ng)))

            # Số ngày
            tk.Label(popup, text=" *", fg="red").grid(row=3, column=0, sticky="e")
            tk.Label(popup, text="Số ngày:").grid(row=3, column=1, padx=5, pady=5, sticky="w")
            so_ng_entry = tk.Entry(popup, textvariable=so_ng, validate="key", validatecommand=self.__vcmd, width=30)
            so_ng_entry.grid(row=3, column=2, padx=5, pady=5)

        # Function to save the updated information
        def save_changes(nv):
            """Save the change, used for save button"""
            nv._ho_ten = ho_ten.get()
            nv._luong_cb = luong_cb.get()
            nv._so_sp = so_sp.get() if so_sp != None else None
            nv._so_ng = so_ng.get() if so_ng != None else None

            if nv.is_missing_data():
                # Thông báo lỗi
                messagebox.showerror("Thông báo", f"Vui lòng nhập đầy đủ thông tin yêu cầu!", parent=popup)
            else:
                self.__controller.edit_nv(nv)
                # Show confirmation message
                messagebox.showinfo("Thông báo",f"Thông tin nhân viên cập nhật!\nMã NV: {nv._ma_nv}")
                self.refresh_data(self.__controller.refresh_data())
                popup.destroy()

        # Button to save changes
        save_button = tk.Button(popup, text="Save Changes", command=partial(save_changes, nv))
        save_button.grid(row=4, column=2, padx=5, pady=5)

    # Function to show the popup for editing employee details
    def show_add_popup(self):
        """Show add nv popup"""
        # Create a new window (popup) for editing information
        popup = tk.Toplevel(self)
        popup.title("Thêm nhân viên")
        popup.geometry("310x250")

        NVCommon.show_center_of_window(popup)

        # Họ và tên
        tk.Label(popup, text=" *", fg="red").grid(row=0, column=0, sticky="e")
        tk.Label(popup, text="Họ và tên:", anchor="w").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ho_ten_entry = tk.Entry(popup, width=30)
        ho_ten_entry.grid(row=0, column=2, padx=5, pady=5)

        # Lương cơ bản
        tk.Label(popup, text=" *", fg="red").grid(row=1, column=0, sticky="e")
        tk.Label(popup, text="Lương cơ bản:").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        luong_cb_entry = tk.Entry(popup, validate="key", validatecommand=self.__vcmd, width=30)
        luong_cb_entry.grid(row=1, column=2, padx=5, pady=5)

        # số sản phẩm
        tk.Label(popup, text=" *", fg="red").grid(row=3, column=0, sticky="e")
        so_sp_lb = tk.Label(popup, text="Số sản phẩm:")
        so_sp_entry = tk.Entry(popup, validate="key", validatecommand=self.__vcmd, width=30)

        # số ngày
        so_ng_lb = tk.Label(popup, text="Số ngày:")
        so_ng_entry = tk.Entry(popup, validate="key", validatecommand=self.__vcmd, width=30)
        so_ng_lb.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        so_ng_entry.grid(row=3, column=2, padx=5, pady=5)

        def on_select(event):
            selected_value = combo.get()

            if selected_value == "Nhân Viên VP":
                so_ng_lb.grid(row=3, column=1, padx=5, pady=5, sticky="w")
                so_ng_entry.grid(row=3, column=2, padx=5, pady=5)

                so_sp_lb.grid_forget()
                so_sp_entry.grid_forget()
            else:
                so_sp_lb.grid(row=3, column=1, padx=5, pady=5, sticky="w")
                so_sp_entry.grid(row=3, column=2, padx=5, pady=5)

                so_ng_lb.grid_forget()
                so_ng_entry.grid_forget()

        # Loại nhân viên
        loai_nv_lb = tk.Label(popup, text="Loại NV:")
        loai_nv_lb.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        combo = ttk.Combobox(popup, values=["Nhân Viên VP", "Nhân Viên BH"], state="readonly", width=27)
        combo.set("Nhân Viên VP")
        combo.bind("<<ComboboxSelected>>", on_select)
        combo.grid(row=2, column=2, padx=5, pady=5)

        # Function to save the updated information
        def save_changes():
            """Save the new nv, use for save button"""
            nhanvien = None
            ho_ten = ho_ten_entry.get()
            luong_cb = luong_cb_entry.get()
            selected_value = combo.get()
            if selected_value == "Nhân Viên VP":
                so_ng = so_ng_entry.get()
                nhanvien = NVVanPhong(None, ho_ten, luong_cb, so_ng, None)
            else:
                so_sp = so_sp_entry.get()
                nhanvien = NVBanHang(None, ho_ten, luong_cb, so_sp, None)

            if nhanvien.is_missing_data():
                # Thông báo lỗi
                messagebox.showerror("Thông báo", f"Vui lòng nhập đầy đủ thông tin yêu cầu!", parent=popup)
            else:
                self.__controller.insert_nv(nhanvien)
                # Show confirmation message
                messagebox.showinfo("Information",
                                    f"Nhân viên đã được thêm!")
                self.refresh_data(self.__controller.refresh_data())
                popup.destroy()

        # Button to save changes
        save_button = tk.Button(popup, text="Save Changes", command=save_changes)
        save_button.grid(row=4, column=2, padx=5, pady=5)

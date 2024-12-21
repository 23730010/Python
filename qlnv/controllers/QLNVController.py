from qlnv.models.CongTy import CongTy
from qlnv.services.DSNhanVienService import DSNhanVienService
from qlnv.views.DanhSachNVView import DanhSachNVView


class QLNVController:

    def __init__(self, login_controller, user):
        self.__login_controller = login_controller
        self.__user = user
        self.__ds_nv_service = DSNhanVienService()
        self.__ct = CongTy(789, 'TNHH MTV UIT')
        self.__ds_nv_view = None

    @property
    def user(self):
        return self.__user

    def start(self):
        """Start QLNV feature"""
        self.show_ds_nv()

    def get_ten_cty(self):
        """Get ten cty"""
        return self.__ct.get_ten_cty

    def show_ds_nv(self):
        """Show list of nv"""
        self.__ds_nv_view = DanhSachNVView(self)
        self.__ds_nv_view.show_nv_list(self.__ds_nv_service.find_all_nv())
        self.__ds_nv_view.mainloop()

    def refresh_data(self):
        """Refresh data"""
        return self.__ds_nv_service.find_all_nv()

    def edit_nv(self, nv):
        """Edit nv"""
        self.__ds_nv_service.update_nv(nv)

    def insert_nv(self, nv):
        """Insert nv"""
        self.__ds_nv_service.insert_nv(nv)

    def delete_nv(self, nv):
        """Delete nv"""
        self.__ds_nv_service.delete_nv(nv)

    def search_nv(self, ma_nv, ho_ten):
        """Search nv"""
        return self.__ds_nv_service.search_nv(ma_nv, ho_ten)

    def tinh_luong(self, nv):
        """Tính lương"""
        self.__ds_nv_service.calculate_salary(nv)

    def logout(self):
        """Logout"""
        self.__ds_nv_view.destroy()
        self.__login_controller.open_login_screen(self)

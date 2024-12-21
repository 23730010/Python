from qlnv.models.NVVanPhong import NVVanPhong
from qlnv.repositories.NhanVienRepository import NhanVienRepository


class DSNhanVienService:
    def __init__(self):
        self.__nhan_vien_repo = NhanVienRepository()

    def calculate_salary(self, nv):
        """Calculate salary"""
        nv.tinh_luong()
        self.__nhan_vien_repo.update_nv(nv)

    def update_nv(self, nv):
        """update nv"""
        if nv._luong_ht != None:
            nv.tinh_luong()
        self.__nhan_vien_repo.update_nv(nv)

    def insert_nv(self, nv):
        """insert nv"""
        self.__nhan_vien_repo.insert_nv(nv)

    def delete_nv(self, nv):
        """delete nv"""
        self.__nhan_vien_repo.delete_nv(nv)

    def search_nv(self, ma_nv, ho_ten):
        """search nv"""
        return self.__nhan_vien_repo.search_nv_by_manv_hoten(ma_nv, ho_ten)

    def find_all_nv(self):
        """find all nv"""
        return self.__nhan_vien_repo.find_all_nv()

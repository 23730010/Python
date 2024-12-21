from typing_extensions import override

from qlnv.models.NhanVien import NhanVien


class NVBanHang(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_sp, luong_ht):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self._so_sp = so_sp
        self._luong_ht = luong_ht

    @override
    def tinh_luong(self):
        self._luong_ht = float(self._luong_cb) + float(self._so_sp) * 18
        return self._luong_ht

    @override
    def is_missing_data(self):
        if not self._ho_ten or not self._luong_cb or not self._so_sp:
            return True
        else:
            return False

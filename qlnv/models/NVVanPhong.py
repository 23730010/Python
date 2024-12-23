from typing import override

from qlnv.models.NhanVien import NhanVien


class NVVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_cb, so_ng, luong_ht):
        super().__init__(ma_nv, ho_ten, luong_cb)
        self._so_ng = so_ng
        self._luong_ht = luong_ht

    @override
    def tinh_luong(self):
        """Tính Lương"""
        self._luong_ht = float(self._luong_cb) + float(self._so_ng) * 180_000
        return self._luong_ht

    @override
    def is_missing_data(self):
        """Check missing data of nv when adding or editing nv"""
        if not self._ho_ten or not self._luong_cb or not self._so_ng:
            return True
        else:
            return False

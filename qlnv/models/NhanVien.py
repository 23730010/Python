from abc import ABC, abstractmethod


class NhanVien(ABC):
    def __init__(self, ma_nv, ho_ten, luong_cb):
        self._ma_nv = ma_nv
        self._ho_ten = ho_ten
        self._luong_cb = luong_cb
        self._luong_ht = 0

    @abstractmethod
    def tinh_luong(self):
        pass

    @abstractmethod
    def is_missing_data(self):
        pass

    def __str__(self):
        return str([self._ma_nv, self._ho_ten, self._luong_cb, self._luong_ht])

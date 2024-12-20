from qlnv.repositories.NhanVienRepository import NhanVienRepository


class CongTy:
    def __init__(self, ma_ct, ten_ct):
        self.__ma_ct = ma_ct
        self.__ten_ct = ten_ct
        self.__ds = []
        self.__nhan_vien_repo = NhanVienRepository()

    @property
    def ds(self):
        return self.__ds

    @property
    def get_ten_cty(self):
        return self.__ten_ct

    @property
    def set_ds(self, ds):
        self.__ds = ds

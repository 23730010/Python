import encodings
from encodings.utf_8 import encode

from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

# Base class for ORM models
Base = declarative_base()


# Define 'NHAN_VIEN' table
class NhanVienEntity(Base):
    __tablename__ = 'NHAN_VIEN'# Table name

    ma_nv = Column(Integer, primary_key=True, autoincrement=True)  # Auto-increment field
    ho_ten = Column(String, nullable=False)
    luong_cb = Column(Numeric(19,0), nullable=False)
    luong_ht = Column(Numeric(19, 0), nullable=False)
    so_sp = Column(Integer, nullable=False)
    so_ng = Column(Integer, nullable=False)
    loai_nv = Column(Integer, nullable=False, name="ma_loai")

    def __repr__(self):
        return f"<NhanVien(ma_nv={self.ma_nv}, ho_ten={self.ho_ten}, loai_nv={self.loai_nv})>"

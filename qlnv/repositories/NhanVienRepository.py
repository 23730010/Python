# pip install pyyaml pyodbc sqlalchemy
import unicodedata
import yaml
from sqlalchemy import create_engine, and_, collate
from sqlalchemy.orm import sessionmaker

from qlnv.entities.NhanVienEntity import NhanVienEntity
from qlnv.models.NVBanHang import NVBanHang
from qlnv.models.NVVanPhong import NVVanPhong
from qlnv.utilities.NVCommon import NVCommon


class NhanVienRepository:
    def __init__(self):
        # Load the YAML configuration
        with open('./resources/datasource.yaml', 'r') as file:
            config = yaml.safe_load(file)['mssql']

        # Database connection
        connection_string = (
            f"mssql+pyodbc://{config['username']}:{config['password']}@"
            f"{config['server']}:{config['port']}/{config['database']}?"
            f"driver={config['driver'].replace(' ', '+')}"
        )
        self.__engine = create_engine(connection_string, echo=True)

    # Normalize function
    def remove_accents(input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join(c for c in nfkd_form if not unicodedata.combining(c))

    def find_all_nv(self):
        results = []
        session = None
        try:
            Session = sessionmaker(bind=self.__engine)
            session = Session()

            # Query data
            nhan_viens = session.query(NhanVienEntity).filter(NhanVienEntity.ma_nv != 0).all()
            for nv in nhan_viens:
                if nv.loai_nv == 1:
                    results.append(NVVanPhong(nv.ma_nv, nv.ho_ten, nv.luong_cb, nv.so_ng, nv.luong_ht))
                else:
                    results.append(NVBanHang(nv.ma_nv, nv.ho_ten, nv.luong_cb, nv.so_sp, nv.luong_ht))
            return results
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def tim_nv_ban_hang(self):
        # Create session
        results = []
        session = None
        try:
            Session = sessionmaker(bind=self.__engine)
            session = Session()

            # Query data
            nhan_viens = session.query(NhanVienEntity).filter(
                and_(NhanVienEntity.loai_nv == 2, NhanVienEntity.ma_nv != 0)).all()
            for nv in nhan_viens:
                print(nv)
                results.append(NVBanHang(nv.ma_nv, nv.ho_ten, nv.luong_cb, nv.so_sp, nv.luong_ht))
            return results
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def tim_nv_van_phong(self):
        # Create session
        results = []
        session = None
        try:
            Session = sessionmaker(bind=self.__engine)
            session = Session()

            # Query data
            nhan_viens = session.query(NhanVienEntity).filter(
                and_(NhanVienEntity.loai_nv == 1, NhanVienEntity.ma_nv != 0)).all()
            for nv in nhan_viens:
                results.append(NVVanPhong(nv.ma_nv, nv.ho_ten, nv.luong_cb, nv.so_ng, nv.luong_ht))
            return results
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def update_nv(self, nv):
        session = None
        try:
            Session = sessionmaker(bind=self.__engine)
            session = Session()

            # Query data
            nhan_vien = session.query(NhanVienEntity).filter(
                and_(NhanVienEntity.ma_nv == nv._ma_nv, NhanVienEntity.ma_nv != 0)).first()
            if nhan_vien:
                # Update the employee's salary
                nhan_vien.ho_ten = nv._ho_ten
                nhan_vien.luong_cb = nv._luong_cb
                if isinstance(nv, NVVanPhong):
                    nhan_vien.so_ng = nv._so_ng
                else:
                    nhan_vien.so_sp = nv._so_sp
                nhan_vien.luong_ht = round(float(nv._luong_ht), 4)
                session.commit()  # Commit the transaction
                print(f"Nhan vien {nhan_vien.ho_ten} đã được cập nhật")
            else:
                print("Employee not found.")
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def insert_nv(self, nv):
        session = None
        try:
            Session = sessionmaker(bind=self.__engine)
            session = Session()

            # Query data
            nhan_vien = None
            if isinstance(nv, NVVanPhong):
                nhan_vien = NhanVienEntity(ho_ten=nv._ho_ten, luong_cb=nv._luong_cb, luong_ht=nv._luong_ht, so_sp=None,
                                           so_ng=nv._so_ng, loai_nv=1)
            else:
                nhan_vien = NhanVienEntity(ho_ten=nv._ho_ten, luong_cb=nv._luong_cb, luong_ht=nv._luong_ht,
                                           so_sp=nv._so_sp, so_ng=None, loai_nv=2)
            session.add(nhan_vien)

            session.commit()  # Commit the transaction
            print(f"Nhân viên {nhan_vien.ho_ten} đã được thêm")
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def delete_nv(self, nv):
        session = None
        try:
            Session = sessionmaker(bind=self.__engine)
            session = Session()

            # Query data
            nhan_vien = session.query(NhanVienEntity).filter(
                and_(NhanVienEntity.ma_nv == nv._ma_nv, NhanVienEntity.ma_nv != 0)).first()
            session.delete(nhan_vien)

            session.commit()  # Commit the transaction
            print(f"Nhan vien {nhan_vien.ho_ten} đã được xóa")
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def search_nv_by_manv_hoten(self, ma_nv, ho_ten):
        if not ma_nv.strip() and not ho_ten.strip():
            return self.find_all_nv()
        else:
            session = None
            results = []
            try:
                Session = sessionmaker(bind=self.__engine)
                session = Session()

                # Query data
                if not ma_nv.strip():
                    search_pattern = f"%{NVCommon.remove_accents(ho_ten)}%"
                    nhan_viens = session.query(NhanVienEntity).filter(
                        and_(NhanVienEntity.ho_ten.collate('Vietnamese_CI_AI').ilike(search_pattern),
                             NhanVienEntity.ma_nv != 0)).all()
                elif not ho_ten.strip():
                    nhan_viens = session.query(NhanVienEntity).filter(
                        and_(NhanVienEntity.ma_nv == ma_nv, NhanVienEntity.ma_nv != 0)).all()
                else:
                    search_pattern = f"%{NVCommon.remove_accents(ho_ten)}%"
                    nhan_viens = session.query(NhanVienEntity).filter(
                        and_(NhanVienEntity.ma_nv != 0, NhanVienEntity.ma_nv == ma_nv,
                             collate(NhanVienEntity.ho_ten, "Vietnamese_CI_AI").ilike(search_pattern))).all()

                for nv in nhan_viens:
                    if nv.loai_nv == 1:
                        results.append(NVVanPhong(nv.ma_nv, nv.ho_ten, nv.luong_cb, nv.so_ng, nv.luong_ht))
                    else:
                        results.append(NVBanHang(nv.ma_nv, nv.ho_ten, nv.luong_cb, nv.so_sp, nv.luong_ht))
                return results
            except Exception as e:
                print("Error:", e)
            finally:
                session.close()

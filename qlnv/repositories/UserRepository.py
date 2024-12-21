# pip install pyyaml pyodbc sqlalchemy
import yaml
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker

from qlnv.entities.UserEntity import UserEntity


class UserRepository:
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
        self.engine = create_engine(connection_string, echo=True)

    def find_user_by_username(self, user_name):
        """find user by username"""
        # Create session
        session = None
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            # Query data
            user = session.query(UserEntity).filter(UserEntity.username == user_name).first()
            return user
        except Exception as e:
            print("Error:", e)
        finally:
            session.close()

    def insert_user(self, user):
        """insert user"""
        # Create session
        session = None
        try:
            Session = sessionmaker(bind=self.engine)
            session = Session()

            user_entity = UserEntity(username=user.get_user_name, password=user.get_encrypt_password)
            # Query data
            session.add(user_entity)
            session.commit()
            print("Tìm thấy user: " + user)
            return 1
        except Exception as e:
            return 0
        finally:
            session.close()

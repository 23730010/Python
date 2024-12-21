from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

# Tạo lớp cơ sở
Base = declarative_base()


# Define Entity for `users` table
class UserEntity(Base):
    __tablename__ = 'USERS'  # table name

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(300), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}')>"

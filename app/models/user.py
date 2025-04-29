from sqlalchemy import Column, BigInteger, String, Enum, Boolean, DateTime, func
from enum import Enum as UserEnum
from app import db

class UserRole(UserEnum):
    ADMIN = 'admin'  # Tài khoản với cấp độ cao nhất
    SUBSCRIBER = 'subscriber'
    MANAGER = 'MANAGER'  # Tài khoản vai trò quản lý
    INTERN = 'INTERN'  # Tài khoản vai trò internship

class UserStatus(UserEnum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BANNED = 'banned'

class User(db.Model):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(Enum(UserRole), default=UserRole.INTERN)
    status = Column(Enum(UserStatus), nullable=False, default=UserStatus.ACTIVE)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    def __str__(self):
        return f"User( id = { self.id }, username = { self.username }, email = { self.email }, password = { self.password }, role = { self.role }, status = { self.status }, is_verified = { self.is_verified }, created_at = { self.created_at } )"
    
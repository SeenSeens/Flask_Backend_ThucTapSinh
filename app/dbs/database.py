from datetime import datetime
from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey, Text, UniqueConstraint
from sqlalchemy.orm import relationship
from app import db
from flask_login import UserMixin
from enum import Enum as UserEnum

class UserRole(UserEnum):
    ADMIN = 'admin' # Tài khoản với cấp độ cao nhất
    EDITOR = 'editor'
    AUTHOR = 'author'
    SUBSCRIBER = 'subscriber'
    MANAGER = 'MANAGER' # Tài khoản vai trò quản lý
    INTERN = 'INTERN' # Tài khoản vai trò internship
class UserStatus(UserEnum):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    BANNED = 'banned'
# User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(50),unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(db.Enum(UserRole), nullable=False, default=UserRole.SUBSCRIBER)
    status = Column(db.Enum(UserStatus), nullable=False, default=UserStatus.ACTIVE)
    created_at = Column(DateTime(), default=datetime.utcnow)
    meta = relationship('UserMeta', backref="user", uselist=False, cascade="all, delete-orphan", lazy=True)
    def __str__(self):
        return f"User( id = { self.id }, username = { self.username }, email = { self.email }, password = { self.password }, role = { self.role }, status = { self.status }, created_at = { self.created_at }, meta = { self.meta } )"



class UserMeta(db.Model):
    __tablename__ = 'user_meta'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('users.id', ondelete="CASCADE"), unique=True, nullable=False)  # dùng string 'users.id'
    meta_key = Column(String(255), unique=True, nullable=False)
    meta_value = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'meta_key', name='uq_user_meta'),
    )

    def __str__(self):
        return f"<UserMeta id={self.id}, user_id={self.user_id}, meta_key={self.meta_key}>"
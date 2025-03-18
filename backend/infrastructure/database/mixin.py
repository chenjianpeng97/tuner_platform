from datetime import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimestampMixin:
    """
    为表自动添加 create_time, update_time 字段
    """

    @declared_attr
    def create_time(cls):
        return Column(DateTime, default=datetime.utcnow)

    @declared_attr
    def update_time(cls):
        return Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@declarative_mixin
class UserAuditMixin:
    """
    为表自动添加 create_by, update_by 字段
    """

    @declared_attr
    def create_by(cls):
        return Column(Integer, nullable=True)  # 假设 create_by 是用户ID

    @declared_attr
    def update_by(cls):
        return Column(Integer, nullable=True)

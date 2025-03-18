from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from .mixin import TimestampMixin, UserAuditMixin
from . import listener  # 导入 listener 模块

Base = declarative_base()


class ProjectDB(TimestampMixin, UserAuditMixin, Base):  # 数据库模型
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String(100), nullable=False)
    description = Column(String(255))  # 可选长度

    test_runs = relationship("TestRunDB", back_populates="project")  # 与 TestRunDB 的关系

    # 可以添加其他的数据库相关的属性或方法


class TestRunDB(TimestampMixin, UserAuditMixin, Base):
    __tablename__ = "test_run"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("project.id"))

    # 明确指定使用哪个外键
    project = relationship("ProjectDB",
                           back_populates="test_runs",
                           foreign_keys=[project_id])  # 明确指定使用 project_id 作为外键


class UserDB(TimestampMixin, UserAuditMixin, Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(50), nullable=False)

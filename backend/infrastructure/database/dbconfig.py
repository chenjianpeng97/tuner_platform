from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base  # 导入你的数据库模型

DATABASE_URL = "sqlite:///d:/dev/project/tuner_platform/local.db"  # SQLite数据库路径

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 创建表 (只在第一次运行时运行):
# Base.metadata.create_all(bind=engine)
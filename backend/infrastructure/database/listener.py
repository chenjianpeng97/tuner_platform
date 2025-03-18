from datetime import datetime
from sqlalchemy import event
from sqlalchemy.orm import Session


# 假设你有一个函数可以获取当前用户 ID
def get_current_user_id():
    #  TODO:  实现获取当前用户 ID 的逻辑 (例如从 JWT Token 中获取)
    #  这个函数应该根据你的身份验证机制来确定
    return 1  # 默认返回 1，用于测试


@event.listens_for(Session, "before_flush")
def before_flush(session, flush_context, instances):
    """
    在 flush 操作之前，自动设置 create_time, update_time, create_by, update_by 字段
    """
    for instance in session.dirty:  # 已经存在的对象 (更新)
        if hasattr(instance, "update_time"):
            instance.update_time = datetime.utcnow()
        if hasattr(instance, "update_by"):
            instance.update_by = get_current_user_id()

    for instance in session.new:  # 新创建的对象 (插入)
        if hasattr(instance, "create_time"):
            instance.create_time = datetime.utcnow()
        if hasattr(instance, "create_by"):
            instance.create_by = get_current_user_id()
        if hasattr(instance, "update_time"):
            instance.update_time = datetime.utcnow()  # 插入时也设置 update_time
        if hasattr(instance, "update_by"):
            instance.update_by = get_current_user_id()  # 插入时也设置 update_by

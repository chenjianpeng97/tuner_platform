-- 创建关联的test_run表
CREATE TABLE IF NOT EXISTS test_run (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_id INTEGER NOT NULL
);

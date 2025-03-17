CREATE TABLE IF NOT EXISTS project (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    creator_id INTEGER NOT NULL,
    CONSTRAINT project_name_length CHECK (length(project_name) <= 100)
);


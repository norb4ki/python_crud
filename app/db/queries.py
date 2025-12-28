GET_TASKS = "SELECT * FROM tasks;"
GET_TASK_BY_ID = "SELECT * FROM tasks WHERE id = $1;"
POST_TASK = """
INSERT INTO tasks (title) 
VALUES ($1)
RETURNING id, title, completed;
"""
COMPLETE_TASK = """
UPDATE tasks SET completed = true WHERE id = $1
RETURNING id, title, completed;
"""
DELETE_TASK = """DELETE FROM tasks WHERE id = $1
RETURNING id;
"""
VALIDATE_CONNECTION = "SELECT 1;"
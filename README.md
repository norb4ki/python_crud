## Python CRUD Tasks API

FastAPI service that exposes a simple tasks CRUD API backed by PostgreSQL
using asyncpg.

### Features
- Create tasks with a title
- List all tasks
- Get a task by id
- Mark a task as completed
- Delete a task

### Tech Stack
- FastAPI
- asyncpg
- PostgreSQL
- python-dotenv

### Project Structure
- `app/main.py`: FastAPI app setup and DB pool lifecycle
- `app/routes/task.py`: HTTP endpoints for tasks
- `app/services/task_manager.py`: Task service layer
- `app/repositories/task_repository.py`: DB access layer
- `app/db/queries.py`: SQL queries
- `app/models/task.py`: Task domain model
- `app/schemas/task.py`: Pydantic schemas

### Requirements
- Python 3.10+
- PostgreSQL running locally on `localhost:5432`

### Environment Variables
Create a `.env` file in the project root:

```
DB_TASKS_USER=your_user
DB_TASKS_PASSWORD=your_password
DB_TASKS_NAME=your_database
```

### Database Setup
Create the `tasks` table:

```sql
CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  completed BOOLEAN NOT NULL DEFAULT FALSE
);
```

### Install Dependencies
Install the core dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the API
```bash
uvicorn app.main:app --reload
```

API will be available at `http://127.0.0.1:8000`.

### Endpoints
- `GET /tasks` - list tasks
- `POST /tasks` - create task, body: `{ "title": "Task title" }`
- `GET /tasks/{id}` - get task by id
- `PATCH /tasks/{id}` - mark task completed
- `DELETE /tasks/{id}` - delete task

### Notes
- DB connection settings are read from `.env`.
- The DB host and port are fixed to `localhost:5432` in `app/main.py`.


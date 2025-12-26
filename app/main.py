from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes.task import router as task_router
from dotenv import load_dotenv
from app.repositories.task_repository import TaskRepository
from app.services.task_manager import TaskService
import asyncpg
import os

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
  # Open the pool on startup
  try:
    app.state.db_pool = await asyncpg.create_pool(
        user=os.getenv('DB_TASKS_USER'), 
        database=os.getenv('DB_TASKS_NAME'), 
        password=os.getenv('DB_TASKS_PASSWORD'),
        host='localhost',
        port=5432
        )
    repo = TaskRepository(app.state.db_pool)
    app.state.tm = TaskService(repo)
  except Exception as e:
    print("Connection failed:")
    print(e)
  
  yield
  # Close the pool after application is finished
  try:
    await app.state.db_pool.close()
    print('Connection is closed')
  except Exception as e:
    print("Exception raised during pool closing:")
    print(e)

app = FastAPI(lifespan=lifespan)
app.include_router(task_router)
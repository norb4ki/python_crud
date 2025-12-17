from fastapi import APIRouter, HTTPException
from app.services.task_manager import TaskManager
from app.schemas.task import TaskModel
router = APIRouter()
tm = TaskManager()

@router.get('/tasks')
async def get_tasks():
  return tm.to_dict()

@router.post('/tasks')
async def post_task(task: TaskModel):
  added_task = tm.add_task(task.title)
  return tm._task_to_dict(added_task)

@router.get('/tasks/{id}')
async def get_task_by_id(id: int):
  try:
    task = tm.get_task(id)
    return tm._task_to_dict(task)
  except KeyError:
    raise HTTPException(
      status_code = 404,
      detail = f"Task with id={id} not found"
      )
  
@router.delete('/tasks/{id}')
async def delete_task_by_id(id: int):
  try:
    task = tm.remove_task(id)
    return tm._task_to_dict(task)
  except KeyError:
    raise HTTPException(
      status_code = 404,
      detail = f"Task with id={id} not found"
      )

@router.patch('/tasks/{id}')
async def complete_task_by_id(id: int):
  try:
    tm.complete_task(id)
  except KeyError:
    raise HTTPException(
      status_code = 404,
      detail = f"Task with id={id} not found"
      )
  
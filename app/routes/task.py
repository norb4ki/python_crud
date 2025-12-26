from fastapi import APIRouter, HTTPException, Request
from app.repositories.task_repository import TaskRepository
from app.services.task_manager import TaskService
from app.schemas.task import *

router = APIRouter(
  prefix='/tasks',
  tags=["tasks"]
  )

@router.get('/', response_model=list[TaskRead])
async def get_tasks(req: Request, ):
  # Retrieving Task Manager from app state
  tm = req.app.state.tm

  return tm.to_dict()

@router.post('/', response_model=TaskRead)
async def post_task(req: Request, task: TaskModel):
    # Retrieving Task Manager from app state
  tm = req.app.state.tm

  added_task = tm.add_task(task.title)
  return tm._task_to_dict(added_task)

@router.get(
    '/{id}', 
    response_model=TaskRead,
    responses={
      404: {"model": NotFoundResponse, "description":f"Not Found"}
    }   
    )
async def get_task_by_id(req: Request, id: int):
  # Retrieving Task Manager from app state
  tm = req.app.state.tm

  try:
    task = tm.get_task(id)
    return tm._task_to_dict(task)
  except KeyError:
    raise HTTPException(
      status_code = 404,
      detail = f"Task with id={id} not found"
      )
  
@router.delete(
    '/{id}', 
    status_code=204,
    responses={
      404: {"model": NotFoundResponse, "description":f"Not Found"}
    }  
    )
async def delete_task_by_id(req: Request, id: int):
  # Retrieving Task Manager from app state
  tm = req.app.state.tm

  try:
    tm.remove_task(id)
    
  except KeyError:
    raise HTTPException(
      status_code = 404,
      detail = f"Task with id={id} not found"
      )

@router.patch(
    '/{id}', 
    response_model=TaskRead,
    responses={
      404: {"model": NotFoundResponse, "description":f"Not Found"}
    }   
    )
async def complete_task_by_id(req: Request, id: int):
  # Retrieving Task Manager from app state
  tm = req.app.state.tm

  try:
    tm.complete_task(id)
    task = tm.get_task(id)
    return tm._task_to_dict(task)
  except KeyError:
    raise HTTPException(
      status_code = 404,
      detail = f"Task with id={id} not found"
      )
  
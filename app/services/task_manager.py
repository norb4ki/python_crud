from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.utils.exceptions import *

class TaskService:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  async def add_task(self, title: str):
    return self.repository.create(title)

  async def complete_task(self, id: int):
    if not self.repository.is_task_exists(id): 
      raise KeyError(f"Task with id {id} wasn't found")
    return self.repository.complete(id)

  async def get_tasks(self):
    """
    Retrieve a list of tasks.

    Returns:
        list[Task]: The list of task objects
    """
    tasks = await self.repository.get_all()
    return list(tasks)

  async def remove_task(self, id: int):
    if not self.repository.is_task_exists(id):
      raise KeyError(f"Task with id {id} wasn't found")
    
    return self.repository.delete(id)

  async def get_task(self, id: int) -> Task:
    """
    Retrieve a task by its unique identifier.

    Args:
        id (int): Unique task ID.

    Returns:
        Task: The task object.

    Raises:
        TaskNotFoundError: If the task does not exist.
    """

    task = await self.repository.get_by_id(id)
    
    if task is None:
      raise TaskNotFoundError(id)

    return task

  def _task_to_dict(self, task: Task):
    return {
      "id": task.id,
      "title": task.title,
      "status": task.status
    }
  
  async def to_dict(self):
    tasks = await self.get_tasks()
    return [self._task_to_dict(task) for task in tasks]
  
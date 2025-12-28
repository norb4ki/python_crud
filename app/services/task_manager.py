from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.utils.exceptions import *

class TaskManager:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  async def add_task(self, title: str):
    """
    Add the task with provided title. 

    Args:
      title (string): Task title.
    
    Returns:
      task: The  Task object
    """
    task = await self.repository.create(title)
    return task

  async def complete_task(self, id: int):
    """
    Mark a task as completed by its unique identifier.

    Args:
      id (int): Unique task ID.

    Returns:
      task: The Task object.

    Raises:
      TaskNotFoundError: If the task does not exist.
    """
    task = await self.repository.complete(id)

    if task is None:
      raise TaskNotFoundError(id)
    return task

  async def get_tasks(self):
    """
    Retrieve a list of tasks.

    Returns:
        list[Task]: The list of task objects
    """
    tasks = await self.repository.get_all()
    return list(tasks)

  async def remove_task(self, id: int):
    """
    Delete a task by its unique id.

    Args:
      id (int): Unique task ID.
    
    Raises:
      TaskNotFoundError: If the task does not exist.
    """
    response = await self.repository.delete(id)
    if not response:
      raise TaskNotFoundError(id)

  async def get_task(self, id: int) -> Task:
    """
    Retrieve a task by its unique id.

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
      "status": task.completed
    }
  
  async def to_dict(self):
    tasks = await self.get_tasks()
    return [self._task_to_dict(task) for task in tasks]
  
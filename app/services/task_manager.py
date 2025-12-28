from app.models.task import Task
from app.repositories.task_repository import TaskRepository


class TaskService:
  def __init__(self, repository: TaskRepository):
    self.repository = repository

  def add_task(self, title: str):
    return self.repository.create(title)

  def complete_task(self, id: int):
    if not self.repository.is_task_exists(id): 
      raise KeyError(f"Task with id {id} wasn't found")
    return self.repository.complete(id)

  async def get_tasks(self):
    tasks = await self.repository.get_all()
    return list(tasks)

  def remove_task(self, id: int):
    if not self.repository.is_task_exists(id):
      raise KeyError(f"Task with id {id} wasn't found")
    
    return self.repository.delete(id)

  def get_task(self, id):
    if not self.repository.is_task_exists(id):
      raise KeyError(f"Task with id {id} wasn't found")
    
    return self.repository.get_by_id(id)

  def _task_to_dict(self, task: Task):
    return {
      "id": task.id,
      "title": task.title,
      "status": task.status
    }
  
  async def to_dict(self):
    tasks = await self.get_tasks()
    return [self._task_to_dict(task) for task in tasks]
  
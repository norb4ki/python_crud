from app.models.task import Task
from app.repositories.task_repository import TaskRepository


class TaskService:
  def __init__(self):
    self.repository = TaskRepository()

  def add_task(self, title: str):
    return self.repository.create(title)

  def complete_task(self, id: int):
    if not self.repository.is_task_exists(id): 
      raise KeyError(f"Task with id {id} wasn't found")
    return self.repository.complete(id)
  

  def get_tasks(self):
    return list(self.repository.get_all())

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
  
  def to_dict(self):
    return [self._task_to_dict(task) for task in self.get_tasks()]
  
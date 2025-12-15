from app.models.task import Task

class TaskManager:
  def __init__(self):
    self._tasks: dict[int, Task] = {}

  def add_task(self, title: str):
    id = len(self._tasks) + 1
    task = Task(id, title)
    self._tasks[id] = task
    return task

  def complete_task(self, id: int):
    if id not in self._tasks: 
      raise KeyError("Task with such id wasn't found")
    else:
      task = self._tasks[id]
      task.completed = True

  def get_tasks(self):
    return list(self._tasks.values())
  
  def pending_tasks(self):
    return (task for task in self._tasks.values() if not task.completed)

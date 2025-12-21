from app.models.task import Task
class TaskRepository:

  def __init__(self):
    self._tasks: dict[int, Task] = {}
    self._next_id = 1

  def get_all(self) -> list[Task]: 
    return list(self._tasks.values())

  def get_by_id(self, id:int) -> Task:
    return self._tasks[id]

  def create(self, title: str) -> Task:
    task = Task(self._next_id, title)
    self._tasks[self._next_id] = task
    self._next_id += 1

    return task

  def delete(self, id: int) -> Task:
    return self._tasks.pop(id)


  def complete(self, id: int) -> Task:
    task = self._tasks[id]
    task.completed = True

    return task
  
  def is_task_exists(self, id: int) -> bool:
    return id in self._tasks
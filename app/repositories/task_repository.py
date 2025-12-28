from app.models.task import Task
from asyncpg import Pool, Record
from app.db.queries import *
class TaskRepository:

  def __init__(self, pool: Pool):
    self._pool = pool
    print('Pool from repo:', self._pool)
    self._tasks: dict[int, Task] = {}
    self._next_id = 1

  async def get_all(self) -> list[Task]: 
    task_records = await self._pool.fetch(GET_TASKS)
    return self._rec_list_to_task_list(task_records)

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
  
  def _record_to_task(self, rec: Record) -> Task:
    return Task(id=rec["id"], title=rec["title"], completed=rec["completed"])
  
  def _rec_list_to_task_list(self, rec: list[Record]) -> list[Task]:
    return [self._record_to_task(record) for record in rec]
  
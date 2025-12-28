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

  async def get_by_id(self, id:int) -> Task | None:
    task_record = await self._pool.fetchrow(GET_TASK_BY_ID, id)
    
    if task_record is None:
      return None
    
    return self._record_to_task(task_record)

  async def create(self, title: str) -> Task:
    task_record = await self._pool.fetchrow(POST_TASK, title)

    return self._record_to_task(task_record)

  async def delete(self, id: int) -> Task:
    return self._tasks.pop(id)


  async def complete(self, id: int) -> Task | None:
    task_record = await self._pool.fetchrow(COMPLETE_TASK, id)
    if task_record is None:
      return None
    
    return self._record_to_task(task_record)
  
  def is_task_exists(self, id: int) -> bool:
    return id in self._tasks
  
  def _record_to_task(self, rec: Record) -> Task:
    return Task(id=rec["id"], title=rec["title"], completed=rec["completed"])
  
  def _rec_list_to_task_list(self, rec: list[Record]) -> list[Task]:
    return [self._record_to_task(record) for record in rec]
  
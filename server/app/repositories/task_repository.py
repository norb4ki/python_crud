from app.models.task import Task
from asyncpg import Pool, Record
from app.db.queries import *
class TaskRepository:

  def __init__(self, pool: Pool):
    self._pool = pool

  async def get_all(self) -> list[Task]: 
    """
    Get the task list from db and return as the list of Task objects.
    """
    task_records = await self._pool.fetch(GET_TASKS)
    return self._rec_list_to_task_list(task_records)

  async def get_by_id(self, id:int) -> Task | None:
    """
    Get the task from db and return as Task object. Return None if there is no row with such id in db.
    """
    task_record = await self._pool.fetchrow(GET_TASK_BY_ID, id)
    
    if task_record is None:
      return None
    
    return self._record_to_task(task_record)

  async def create(self, title: str) -> Task:
    """
    Create a new task with provided title in db. Marks the new task as not completed by default. 
    Returns the new task as Task object.
    """
    task_record = await self._pool.fetchrow(POST_TASK, title)

    return self._record_to_task(task_record)

  async def delete(self, id: int) -> bool:
    """
    Delete the task by provided id from db. Return True if deleted False otherwise.
    """
    record = await self._pool.fetchrow(DELETE_TASK, id)

    return record is not None


  async def complete(self, id: int) -> Task | None:
    """
    Marks the task with provided id as completed in db. Returns Task object on success, None otherwise.
    """
    task_record = await self._pool.fetchrow(COMPLETE_TASK, id)
    if task_record is None:
      return None
    
    return self._record_to_task(task_record)

  
  def _record_to_task(self, rec: Record) -> Task:
    return Task(id=rec["id"], title=rec["title"], completed=rec["completed"])
  
  def _rec_list_to_task_list(self, rec: list[Record]) -> list[Task]:
    return [self._record_to_task(record) for record in rec]
  
from pydantic import BaseModel

class TaskModel(BaseModel):
  title: str

class TaskRead(BaseModel):
  id: int
  title: str
  status: str

class BaseErrorResponse(BaseModel):
  err: str

class NotFoundResponse(BaseErrorResponse):
  err:str = "Resource not found."
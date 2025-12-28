class Task:
  def __init__(self, id: int, title:str, completed:bool = False):
    self.id = id
    self.title = title
    self.completed: bool = completed

  @property
  def status(self):
    return 'done' if self.completed else 'pending'
  
  def __repr__(self):
    return f"Task (id={self.id}, title={self.title}, status={self.status})"
  
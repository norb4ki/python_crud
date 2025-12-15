from app.services.task_manager import TaskManager

tm = TaskManager()
tm.add_task("Begin")
tm.add_task("Press kachat")

for task in tm.pending_tasks():
    print(task)

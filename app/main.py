from app.services.task_manager import TaskManager

tm = TaskManager()
tm.add_task("Begit")
tm.add_task("Press kachat")

for task in tm.pending_tasks():
    print(task)

tm.add_task("Otjumana")
tm.add_task("prisedana")


for task in tm.pending_tasks():
    print(task)

tm.remove_task(1)
tm.complete_task(3)

for task in tm.pending_tasks():
    print(task)
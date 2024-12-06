"""OrderedDicts are less common now, but still useful"""
from collections import OrderedDict

tasks = [
    ("Task 1", "To Do"),
    ("Task 2", "To Do"),
    ("Task 3", "To Do"),
]

task_dict = OrderedDict(tasks)
task_dict["Task 2"] = "Complete"
task_dict.move_to_end("Task 2")

task_dict["Task 4"] = "To Do"
task_dict.move_to_end("Task 4", last=False)

for task, status in task_dict.items():
    print(f"{task}: {status}")

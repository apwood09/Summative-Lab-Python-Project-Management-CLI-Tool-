import pytest
from models.task import Task

def test_task_completion_logic():
    task = Task(title="Test Task", project_id=1)
    assert task.status == "Pending"
    task.mark_complete()
    assert task.status == "Completed"

def test_task_get_by_id():
    tasks = [
        Task("Task A", 1, task_id=101),
        Task("Task B", 1, task_id=102)
    ]
    found = Task.get_by_id(tasks, 102)
    assert found.title == "Task B"
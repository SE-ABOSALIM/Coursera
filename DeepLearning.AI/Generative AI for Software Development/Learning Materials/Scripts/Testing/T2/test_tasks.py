import pytest
from tasks import add_task, remove_task, list_tasks, clear_tasks

@pytest.fixture(autouse=True)
def clean_tasks():
    """Reset the tasks list before each test."""
    clear_tasks()

def test_add_task_success():
    result = add_task("Buy groceries")
    assert "Buy groceries" in result
    assert len(result) == 1

def test_add_task_empty_raises_error():
    with pytest.raises(ValueError, match="Task cannot be empty."):
        add_task("")

def test_remove_task_success():
    add_task("Clean room")
    result = remove_task("Clean room")
    assert "Clean room" not in result
    assert len(result) == 0

def test_remove_task_not_found():
    result = remove_task("Non-existent task")
    assert result == "Task not found."

def test_list_tasks():
    add_task("Task 1")
    add_task("Task 2")
    current_list = list_tasks()
    assert current_list == ["Task 1", "Task 2"]

def test_clear_tasks():
    add_task("Task 1")
    add_task("Task 2")
    msg = clear_tasks()
    assert msg == "Tasks cleared."
    assert list_tasks() == []
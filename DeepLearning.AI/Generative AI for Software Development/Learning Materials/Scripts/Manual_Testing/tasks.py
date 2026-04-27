# Before handling the edge cases
"""
tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed."
    else:
        return "Task not found."

def list_tasks():
    return tasks

# Example usage
print(add_task("Buy groceries"))
print(add_task("Read a book"))
print(list_tasks())
print(remove_task("Read a book"))
print(list_tasks())
"""

# After handling the edge cases. Improved code
tasks = []

def normalize_task(task):
    if not isinstance(task, str):
        return None
    cleaned = task.strip()
    if not cleaned:
        return None
    return cleaned

def task_exists(task):
    normalized = normalize_task(task)
    if normalized is None:
        return False

    normalized_lower = normalized.lower()
    return any(existing.lower() == normalized_lower for existing in tasks)

def add_task(task):
    normalized = normalize_task(task)

    if normalized is None:
        return "Task must be a non-empty string."

    if task_exists(normalized):
        return f"Task '{normalized}' already exists."

    tasks.append(normalized)
    return f"Task '{normalized}' added."

def remove_task(task):
    if not tasks:
        return "There are no tasks to remove."

    normalized = normalize_task(task)
    if normalized is None:
        return "Task must be a non-empty string."

    normalized_lower = normalized.lower()

    for existing in tasks:
        if existing.lower() == normalized_lower:
            tasks.remove(existing)
            return f"Task '{existing}' removed."

    return "Task not found."

def list_tasks():
    if not tasks:
        return "The task list is empty."
    return tasks.copy()


# Example usage
print(add_task("Buy groceries"))
print(add_task("  Read a book  "))
print(add_task("buy groceries"))   # duplicate because case-insensitive
print(add_task("   "))             # invalid
print(add_task(123))               # invalid

print(list_tasks())

print(remove_task("read a book"))  # works
print(remove_task("  BUY GROCERIES  "))  # works
print(remove_task("   "))          # invalid
print(remove_task("Go to gym"))    # not found

print(list_tasks())
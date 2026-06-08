
# ### **Task 3: JSON Handling**

# #### **Load and Save Tasks (JSON)**
# 1. Create a JSON file named `tasks.json` with the following structure:
#    json
#    [
#        {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
#        {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
#        {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
#    ]
   
# 2. Write a Python program to:
#    - Load the tasks from `tasks.json`.
#    - Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
#    - Save any changes back to the `tasks.json` file (e.g., after modifying a task).

# #### **Calculate Task Completion Stats**
# 1. Write a Python function to calculate the following statistics:
#    - **Total tasks**: Count the total number of tasks.
#    - **Completed tasks**: Count the number of completed tasks.
#    - **Pending tasks**: Count the number of tasks that are not completed.
#    - **Average priority**: Calculate the average priority level of all tasks.
   
#    Display these statistics after loading the tasks.

# #### **Convert JSON Data to CSV**
# 1. Write a function to convert the task data in `tasks.json` to a CSV file named `tasks.csv`. The CSV should have the following columns:
#    - ID
#    - Task Name
#    - Completed Status
#    - Priority

#    For example:
   

# csv
#    ID,Task,Completed,Priority
#    1,Do laundry,False,3
#    2,Buy groceries,True,2
#    3,Finish homework,False,1
   
import csv
import json
from pathlib import Path

JSON_FILE = Path(r"/home/zhav3n/Desktop/homework/Lesson 9/tasks.json")
CSV_FILE  = Path(r"/home/zhav3n/Desktop/homework/Lesson 9/tasks.csv")

# ─────────────────────────────────────────────
#  Core helpers
# ─────────────────────────────────────────────

def load_tasks() -> list[dict]:
    """Read tasks from JSON file."""
    return json.loads(JSON_FILE.read_text())

def save_tasks(tasks: list[dict]) -> None:
    """Persist tasks back to JSON file (pretty-printed)."""
    JSON_FILE.write_text(json.dumps(tasks, indent=4))
    print("✔  Changes saved to tasks.json\n")

def display_tasks(tasks: list[dict]) -> None:
    """Print tasks as a formatted table, sorted by priority."""
    if not tasks:
        print("  No tasks found.\n")
        return
    header = f"{'ID':<5} {'Task':<20} {'Done':<8} {'Priority'}"
    print("\n" + header)
    print("─" * len(header))
    for t in sorted(tasks, key=lambda x: x["priority"]):
        done = "✔ Yes" if t["completed"] else "✘ No"
        print(f"{t['id']:<5} {t['task']:<20} {done:<8} {t['priority']}")
    print()

# ─────────────────────────────────────────────
#  ★ NEW: Completion statistics
# ─────────────────────────────────────────────

def show_stats(tasks: list[dict]) -> None:
    """Display task completion statistics."""
    total     = len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending   = total - completed
    avg_pri   = sum(t["priority"] for t in tasks) / total if total else 0

    print("── Task Statistics ─────────────────────")
    print(f"  Total tasks    : {total}")
    print(f"  Completed      : {completed}")
    print(f"  Pending        : {pending}")
    print(f"  Avg priority   : {avg_pri:.1f}")
    print()

# ─────────────────────────────────────────────
#  ★ NEW: JSON → CSV export
# ─────────────────────────────────────────────

def export_to_csv(tasks: list[dict]) -> None:
    """Convert tasks list to tasks.csv."""
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["ID", "Task", "Completed", "Priority"])
        writer.writeheader()
        writer.writerows(
            {"ID": t["id"], "Task": t["task"],
             "Completed": t["completed"], "Priority": t["priority"]}
            for t in tasks
        )
    print(f"✔  Exported {len(tasks)} tasks to '{CSV_FILE}'\n")

# ─────────────────────────────────────────────
#  Mutation helpers (unchanged)
# ─────────────────────────────────────────────

def _find(tasks: list[dict], task_id: int) -> dict | None:
    return next((t for t in tasks if t["id"] == task_id), None)

def mark_complete(tasks: list[dict], task_id: int) -> None:
    task = _find(tasks, task_id)
    if not task:
        print(f"  Task {task_id} not found.\n"); return
    task["completed"] = True
    print(f"  Marked '{task['task']}' as complete.")

def add_task(tasks: list[dict], name: str, priority: int) -> None:
    new_id = max(t["id"] for t in tasks) + 1 if tasks else 1
    tasks.append({"id": new_id, "task": name, "completed": False, "priority": priority})
    print(f"  Added task [{new_id}] '{name}'.")

def delete_task(tasks: list[dict], task_id: int) -> None:
    task = _find(tasks, task_id)
    if not task:
        print(f"  Task {task_id} not found.\n"); return
    tasks.remove(task)
    print(f"  Deleted task [{task_id}] '{task['task']}'.")

# ─────────────────────────────────────────────
#  Demo
# ─────────────────────────────────────────────

if __name__ == "__main__":

    # ── Load, display & stats ─────────────────
    print("══ Load Tasks ═══════════════════════════")
    tasks = load_tasks()
    display_tasks(tasks)
    show_stats(tasks)

    # ── Export original to CSV ────────────────
    print("══ Export to CSV (original) ═════════════")
    export_to_csv(tasks)
    print(CSV_FILE.read_text())

    # ── Mutations ─────────────────────────────
    print("══ Apply changes ════════════════════════")
    mark_complete(tasks, task_id=1)
    add_task(tasks, name="Read a book", priority=2)
    delete_task(tasks, task_id=2)
    save_tasks(tasks)

    # ── Stats after changes ───────────────────
    print("══ Updated Stats ════════════════════════")
    display_tasks(tasks)
    show_stats(tasks)

    # ── Export updated list to CSV ────────────
    print("══ Export to CSV (updated) ══════════════")
    export_to_csv(tasks)
    print(CSV_FILE.read_text())
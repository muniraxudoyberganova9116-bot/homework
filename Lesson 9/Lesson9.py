# #### Task 1: Create a Library Management System with Custom Exceptions
# 1. Create a Python program to manage a small library system. 
# 2. Define custom exceptions for specific scenarios:
#    - **`BookNotFoundException`**: Raised when trying to borrow a book that doesn’t exist in the library.
#    - **`BookAlreadyBorrowedException`**: Raised when a book is already borrowed.
#    - **`MemberLimitExceededException`**: Raised when a member tries to borrow more books than allowed.
# 3. Implement classes for:
#    - **`Book`**: Attributes include `title`, `author`, and `is_borrowed`.
#    - **`Member`**: Attributes include `name`, `borrowed_books` (limit to 3 books per member).
#    - **`Library`**: Manages books and members, including borrowing and returning books.
# 4. Test your program with the following scenarios:
#    - Adding books and members.
#    - Borrowing and returning books.
#    - Handling exceptions when rules are violated.
class BookNotFoundException(Exception):
    def __init__(self, title=""):
        super().__init__(f"Book not found in the library: '{title}'" if title else "Book not found in the library.")


class BookAlreadyBorrowedException(Exception):
    def __init__(self, title=""):
        super().__init__(f"'{title}' is already borrowed." if title else "Book is already borrowed.")


class MemberLimitExceededException(Exception):
    MAX_BOOKS = 3

    def __init__(self, name=""):
        super().__init__(
            f"'{name}' has reached the {MemberLimitExceededException.MAX_BOOKS}-book borrow limit."
            if name else "Member borrow limit exceeded."
        )


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __repr__(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"Book('{self.title}' by {self.author} [{status}])"


class Member:
    MAX_BORROW_LIMIT = 3

    def __init__(self, name: str):
        self.name = name
        self.borrowed_books: list[Book] = []

    def __repr__(self):
        return f"Member('{self.name}', books={[b.title for b in self.borrowed_books]})"


class Library:
    def __init__(self):
        self._books: dict[str, Book] = {}       # title → Book
        self._members: dict[str, Member] = {}   # name  → Member


    def add_book(self, book: Book) -> None:
        self._books[book.title] = book
        print(f"  [+] Added book    : {book}")

    def add_member(self, member: Member) -> None:
        self._members[member.name] = member
        print(f"  [+] Added member  : {member.name}")


    def borrow_book(self, member_name: str, book_title: str) -> None:
        member = self._get_member(member_name)
        book   = self._get_book(book_title)

        if len(member.borrowed_books) >= Member.MAX_BORROW_LIMIT:
            raise MemberLimitExceededException(member_name)
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(book_title)

        book.is_borrowed = True
        member.borrowed_books.append(book)
        print(f"  ✔  '{member_name}' borrowed '{book_title}'")

    def return_book(self, member_name: str, book_title: str) -> None:
        member = self._get_member(member_name)

        book = next((b for b in member.borrowed_books if b.title == book_title), None)
        if not book:
            raise ValueError(f"'{member_name}' has not borrowed '{book_title}'.")

        book.is_borrowed = False
        member.borrowed_books.remove(book)
        print(f"  ↩  '{member_name}' returned '{book_title}'")


    def _get_book(self, title: str) -> Book:
        book = self._books.get(title)
        if not book:
            raise BookNotFoundException(title)
        return book

    def _get_member(self, name: str) -> Member:
        member = self._members.get(name)
        if not member:
            raise ValueError(f"Member not found: '{name}'")
        return member

    def status(self) -> None:
        print("\n  ── Library Status ──────────────────")
        for book in self._books.values():
            print(f"    {book}")
        for member in self._members.values():
            print(f"    {member}")
        print()


def run_test(label: str, fn):
    print(f"\n{'─'*50}")
    print(f"  TEST: {label}")
    print('─'*50)
    try:
        fn()
    except (BookNotFoundException,
            BookAlreadyBorrowedException,
            MemberLimitExceededException,
            ValueError) as e:
        print(f"  ✘  Exception caught → {e}")


if __name__ == "__main__":
    library = Library()

    print("\n══ Setup ════════════════════════════════")
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
    library.add_book(Book("1984", "George Orwell"))
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_member(Member("Alice"))
    library.add_member(Member("Bob"))

    # ── Test 1: Normal borrow ─────────────────
    run_test("Normal borrow", lambda: (
        library.borrow_book("Alice", "The Great Gatsby"),
        library.borrow_book("Alice", "1984"),
    ))

    run_test("Borrow an already-borrowed book", lambda:
        library.borrow_book("Bob", "The Great Gatsby")   # Alice has it
    )

    run_test("Borrow a non-existent book", lambda:
        library.borrow_book("Alice", "Unknown Title")
    )

    run_test("Exceed 3-book borrow limit", lambda: (
        library.borrow_book("Alice", "To Kill a Mockingbird"),   # 3rd book — OK
        library.borrow_book("Alice", "Brave New World"),         # 4th → exception
    ))

    run_test("Return then re-borrow", lambda: (
        library.return_book("Alice", "The Great Gatsby"),
        library.borrow_book("Bob", "The Great Gatsby"),   # now available
    ))

    run_test("Return a book not borrowed by member", lambda:
        library.return_book("Alice", "Brave New World")
    )

    print("\n══ Final Status ═════════════════════════")
    library.status()


# #### Task 2: Student Grades Management
# 1. Create a CSV file named `grades.csv` with the following structure:
#    csv
#    Name,Subject,Grade
#    Alice,Math,85
#    Bob,Science,78
#    Carol,Math,92
#    Dave,History,74
   
# 2. Write a Python program to:
#    - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
#    - Calculate the average grade for each subject.
#    - Write a new CSV file named `average_grades.csv` with the following structure:
#      csv
#      Subject,Average Grade
#      Math,88.5
#      Science,78
#      History,74
     
# 3. Use the `csv` module for reading and writing the CSV files.

# ---

import csv
from collections import defaultdict

INPUT_FILE  = "grades.csv"
OUTPUT_FILE = "average_grades.csv"

with open(INPUT_FILE, newline="") as f:
    records = list(csv.DictReader(f))          # [{'Name':..., 'Subject':..., 'Grade':...}, ...]

subject_grades: dict[str, list[float]] = defaultdict(list)

for row in records:
    subject_grades[row["Subject"]].append(float(row["Grade"]))

averages = {
    subject: sum(grades) / len(grades)
    for subject, grades in subject_grades.items()
}

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["Subject", "Average Grade"])
    writer.writeheader()
    writer.writerows(
        {"Subject": subject, "Average Grade": avg}
        for subject, avg in averages.items()
    )

print(f"{'Subject':<12} {'Average Grade':>13}")
print("-" * 26)
for subject, avg in averages.items():
    print(f"{subject:<12} {avg:>13.1f}")

print(f"\n✔  Results saved to '{OUTPUT_FILE}'")



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

    
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
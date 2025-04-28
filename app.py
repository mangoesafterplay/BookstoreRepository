from domain.entities import Book
from infrastructure.memory_book_repository import InMemoryBookRepository

# Initialize repository
book_repo = InMemoryBookRepository()

# Add some books
book_repo.add(Book(id=1, title="Clean Code", author="Robert C. Martin", price=29.99))
book_repo.add(Book(id=2, title="Domain-Driven Design", author="Eric Evans", price=49.99))

# Fetch all books
books = book_repo.list()
for book in books:
    print(f"{book.title} by {book.author} - ${book.price}")

# Find a specific book
book = book_repo.get_by_id(1)
print(f"\nFound book: {book.title}")

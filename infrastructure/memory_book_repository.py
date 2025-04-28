from typing import List
from domain.entities import Book
from domain.repositories import BookRepository

class InMemoryBookRepository(BookRepository):
    def __init__(self):
        self._books = {}

    def get_by_id(self, book_id: int) -> Book:
        return self._books.get(book_id)

    def list(self) -> List[Book]:
        return list(self._books.values())

    def add(self, book: Book) -> None:
        self._books[book.id] = book

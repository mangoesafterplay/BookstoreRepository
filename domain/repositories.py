from abc import ABC, abstractmethod
from typing import List
from .entities import Book

class BookRepository(ABC):
    @abstractmethod
    def get_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def list(self) -> List[Book]:
        pass

    @abstractmethod
    def add(self, book: Book) -> None:
        pass

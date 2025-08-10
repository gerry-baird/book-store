from data.book import Book
from typing import List


def initialize_books() -> List[Book]:
    """
    Generate a list of sample books for the application.

    Returns:
        List[Book]: A list of Book objects with sample data
    """
    return [
        Book(
            id=1,
            title="To Kill a Mockingbird",
            author="Harper Lee",
            description="A novel about racial inequality and moral growth in the American South",
            price=12.99,
            condition="good"
        ),
        Book(
            id=2,
            title="1984",
            author="George Orwell",
            description="A dystopian novel about totalitarianism and surveillance",
            price=10.50,
            condition="new"
        ),
        Book(
            id=3,
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
            description="A story of wealth, love, and the American Dream in the Roaring Twenties",
            price=9.99,
            condition="fair"
        ),
        Book(
            id=4,
            title="Harry Potter and the Philosopher's Stone",
            author="J.K. Rowling",
            description="The first book in the Harry Potter series about a young wizard",
            price=15.99,
            condition="new"
        ),
        Book(
            id=5,
            title="The Lord of the Rings",
            author="J.R.R. Tolkien",
            description="An epic fantasy adventure about the quest to destroy the One Ring",
            price=18.75,
            condition="good"
        )
    ]
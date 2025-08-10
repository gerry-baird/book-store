from fastapi import FastAPI, Query
from data.book import Book
from typing import List

app = FastAPI()

# Sample book data
books = [
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


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/books", response_model=List[Book])
async def get_books():
    """Return a list of all available books"""
    return books


@app.get("/title-search", response_model=List[Book])
async def search_books_by_title(query: str = Query(..., description="Search query for book titles")):
    """Search for books by title (case-insensitive)"""
    query = query.lower()
    matching_books = [book for book in books if query in book.title.lower()]
    return matching_books

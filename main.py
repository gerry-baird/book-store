from fastapi import FastAPI, Query, HTTPException
from data.book import Book
from data.generate_data import initialize_books
from typing import List

app = FastAPI()

# Initialize sample book data
books = initialize_books()


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


@app.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    """Return a specific book by its ID"""
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")


@app.get("/title-search", response_model=List[Book])
async def search_books_by_title(query: str = Query(..., description="Search query for book titles")):
    """Search for books by title (case-insensitive)"""
    query = query.lower()
    matching_books = [book for book in books if query in book.title.lower()]
    return matching_books

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This project uses `uv` for dependency management and FastAPI for the web framework.

**Start the development server:**
```bash
uv run fastapi dev main.py
```

**Run the application in production mode:**
```bash
uv run fastapi run main.py --port 8000 --host 0.0.0.0
```

**Install dependencies:**
```bash
uv sync
```

**Docker commands:**
```bash
# Build the Docker image
docker build -t book-store .

# Run the container
docker run -p 8000:8000 book-store
```

## Code Architecture

This is a FastAPI-based book store API with a simple in-memory data structure.

**Project Structure:**
- `main.py` - FastAPI application entry point with basic routes
- `routers/books.py` - Book-related endpoints organized in a router
- `data/book.py` - Pydantic model defining the Book schema
- `data/customer.py` - Pydantic model defining the Customer schema
- `data/order.py` - Pydantic models defining the Order and OrderItem schemas
- `data/generate_data.py` - Sample data initialization functions for books, customers, and orders
- `pyproject.toml` - Project configuration and dependencies using uv

**API Endpoints:**
- `GET /` - Root endpoint returning hello message
- `GET /hello/{name}` - Personalized greeting
- `GET /books` - Returns all books
- `GET /books/{book_id}` - Returns specific book by ID
- `GET /title-search?query=...` - Search books by title (case-insensitive)

**Data Layer:**
- Uses Pydantic models for data validation and serialization
- Book model includes id, title, author, description, price, and condition fields
- Customer model includes id, name, email, phone, address, country, date_joined, is_active, and loyalty_points fields
- Order model includes id, customer_id, order_date, status, items, pricing details, and shipping information
- OrderItem model includes id, book_id, quantity, unit_price, and total_price
- Data is stored in memory as lists initialized at startup from `data/generate_data.py`
- No persistent database - data resets on server restart

**Key Patterns:**
- All endpoints use async/await
- Response models are explicitly defined using Pydantic
- HTTPException for error handling (e.g., 404 for book not found)
- Query parameters use FastAPI's Query for validation and documentation
from pydantic import BaseModel, Field
from typing import Optional, Literal


class Book(BaseModel):
    """Data model representing a book in the store."""
    id: Optional[int] = Field(default=None, description="Unique identifier for the book")
    title: str = Field(..., description="Title of the book")
    author: str = Field(..., description="Author of the book")
    description: Optional[str] = Field(default=None, description="Description of the book")
    price: float = Field(..., description="Price of the book")
    condition: Literal["new", "good", "fair", "poor"] = Field(default="new", description="Physical condition of the book")

from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class Customer(BaseModel):
    """Data model representing a customer in the store."""
    id: Optional[int] = Field(default=None, description="Unique identifier for the customer")
    first_name: str = Field(..., description="Customer's first name")
    last_name: str = Field(..., description="Customer's last name")
    email: str = Field(..., description="Customer's email address")
    phone: Optional[str] = Field(default=None, description="Customer's phone number")
    address: Optional[str] = Field(default=None, description="Customer's street address")
    city: Optional[str] = Field(default=None, description="Customer's city")
    state: Optional[str] = Field(default=None, description="Customer's state/province")
    postal_code: Optional[str] = Field(default=None, description="Customer's postal/zip code")
    country: str = Field(default="US", description="Customer's country")
    date_joined: datetime = Field(default_factory=datetime.now, description="Date customer joined")
    is_active: bool = Field(default=True, description="Whether the customer account is active")
    loyalty_points: int = Field(default=0, description="Customer's loyalty reward points")
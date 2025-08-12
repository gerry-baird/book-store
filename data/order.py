from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime
from decimal import Decimal


class OrderItem(BaseModel):
    """Data model representing an item in an order."""
    id: Optional[int] = Field(default=None, description="Unique identifier for the order item")
    book_id: int = Field(..., description="ID of the book being ordered")
    quantity: int = Field(..., gt=0, description="Quantity of the book ordered")
    unit_price: Decimal = Field(..., gt=0, description="Price per unit at time of order")
    total_price: Decimal = Field(..., gt=0, description="Total price for this line item")


class Order(BaseModel):
    """Data model representing a customer order."""
    id: Optional[int] = Field(default=None, description="Unique identifier for the order")
    customer_id: int = Field(..., description="ID of the customer who placed the order")
    order_date: datetime = Field(default_factory=datetime.now, description="Date and time the order was placed")
    status: Literal["pending", "processing", "shipped", "delivered", "cancelled"] = Field(
        default="pending", description="Current status of the order"
    )
    items: List[OrderItem] = Field(..., description="List of items in the order")
    subtotal: Decimal = Field(..., gt=0, description="Subtotal before tax and shipping")
    tax_amount: Decimal = Field(default=Decimal("0.00"), ge=0, description="Tax amount")
    shipping_amount: Decimal = Field(default=Decimal("0.00"), ge=0, description="Shipping cost")
    total_amount: Decimal = Field(..., gt=0, description="Total order amount")
    shipping_address: Optional[str] = Field(default=None, description="Shipping address for the order")
    notes: Optional[str] = Field(default=None, description="Additional notes about the order")
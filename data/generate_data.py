from data.book import Book
from data.customer import Customer
from data.order import Order, OrderItem
from typing import List
from datetime import datetime, timedelta
from decimal import Decimal


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


def initialize_customers() -> List[Customer]:
    """
    Generate a list of sample customers for the application.

    Returns:
        List[Customer]: A list of Customer objects with sample data
    """
    return [
        Customer(
            id=1,
            first_name="John",
            last_name="Smith",
            email="john.smith@email.com",
            phone="555-0123",
            address="123 Main St",
            city="New York",
            state="NY",
            postal_code="10001",
            country="US",
            date_joined=datetime.now() - timedelta(days=365),
            is_active=True,
            loyalty_points=150
        ),
        Customer(
            id=2,
            first_name="Sarah",
            last_name="Johnson",
            email="sarah.johnson@email.com",
            phone="555-0456",
            address="456 Oak Ave",
            city="Los Angeles",
            state="CA",
            postal_code="90210",
            country="US",
            date_joined=datetime.now() - timedelta(days=180),
            is_active=True,
            loyalty_points=320
        ),
        Customer(
            id=3,
            first_name="Michael",
            last_name="Brown",
            email="michael.brown@email.com",
            phone="555-0789",
            address="789 Pine St",
            city="Chicago",
            state="IL",
            postal_code="60601",
            country="US",
            date_joined=datetime.now() - timedelta(days=90),
            is_active=True,
            loyalty_points=75
        ),
        Customer(
            id=4,
            first_name="Emily",
            last_name="Davis",
            email="emily.davis@email.com",
            phone="555-0321",
            address="321 Elm Dr",
            city="Austin",
            state="TX",
            postal_code="78701",
            country="US",
            date_joined=datetime.now() - timedelta(days=30),
            is_active=True,
            loyalty_points=25
        ),
        Customer(
            id=5,
            first_name="Robert",
            last_name="Wilson",
            email="robert.wilson@email.com",
            phone="555-0654",
            address="654 Maple Ln",
            city="Seattle",
            state="WA",
            postal_code="98101",
            country="US",
            date_joined=datetime.now() - timedelta(days=500),
            is_active=False,
            loyalty_points=0
        )
    ]


def initialize_orders() -> List[Order]:
    """
    Generate a list of sample orders for the application.

    Returns:
        List[Order]: A list of Order objects with sample data
    """
    return [
        Order(
            id=1,
            customer_id=1,
            order_date=datetime.now() - timedelta(days=30),
            status="delivered",
            items=[
                OrderItem(
                    id=1,
                    book_id=1,
                    quantity=1,
                    unit_price=Decimal("12.99"),
                    total_price=Decimal("12.99")
                ),
                OrderItem(
                    id=2,
                    book_id=2,
                    quantity=2,
                    unit_price=Decimal("10.50"),
                    total_price=Decimal("21.00")
                )
            ],
            subtotal=Decimal("33.99"),
            tax_amount=Decimal("2.72"),
            shipping_amount=Decimal("5.99"),
            total_amount=Decimal("42.70"),
            shipping_address="123 Main St, New York, NY 10001",
            notes="Gift wrap requested"
        ),
        Order(
            id=2,
            customer_id=2,
            order_date=datetime.now() - timedelta(days=15),
            status="shipped",
            items=[
                OrderItem(
                    id=3,
                    book_id=4,
                    quantity=1,
                    unit_price=Decimal("15.99"),
                    total_price=Decimal("15.99")
                )
            ],
            subtotal=Decimal("15.99"),
            tax_amount=Decimal("1.44"),
            shipping_amount=Decimal("3.99"),
            total_amount=Decimal("21.42"),
            shipping_address="456 Oak Ave, Los Angeles, CA 90210"
        ),
        Order(
            id=3,
            customer_id=3,
            order_date=datetime.now() - timedelta(days=5),
            status="processing",
            items=[
                OrderItem(
                    id=4,
                    book_id=5,
                    quantity=1,
                    unit_price=Decimal("18.75"),
                    total_price=Decimal("18.75")
                ),
                OrderItem(
                    id=5,
                    book_id=3,
                    quantity=1,
                    unit_price=Decimal("9.99"),
                    total_price=Decimal("9.99")
                )
            ],
            subtotal=Decimal("28.74"),
            tax_amount=Decimal("2.30"),
            shipping_amount=Decimal("4.99"),
            total_amount=Decimal("36.03"),
            shipping_address="789 Pine St, Chicago, IL 60601"
        ),
        Order(
            id=4,
            customer_id=4,
            order_date=datetime.now() - timedelta(days=2),
            status="pending",
            items=[
                OrderItem(
                    id=6,
                    book_id=2,
                    quantity=3,
                    unit_price=Decimal("10.50"),
                    total_price=Decimal("31.50")
                )
            ],
            subtotal=Decimal("31.50"),
            tax_amount=Decimal("2.52"),
            shipping_amount=Decimal("5.99"),
            total_amount=Decimal("40.01"),
            shipping_address="321 Elm Dr, Austin, TX 78701",
            notes="Express shipping requested"
        )
    ]
from data.book import Book
from data.customer import Customer
from typing import List
from datetime import datetime, timedelta


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
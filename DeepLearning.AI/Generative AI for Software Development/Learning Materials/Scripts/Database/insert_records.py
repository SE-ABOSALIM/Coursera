"""
seed_ecommerce_db.py

Simple script to insert some sample records into the ecommerce.db database.

Assumptions:
    - The schema (User, Product, Order, OrderItem) is already created.
    - You have ecommerce_db.py (from the previous step) in the same directory.

This script:
    1. Creates a few users and products.
    2. Creates an order for one user.
    3. Adds order items for that order.
"""

from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Import the models and Base from your schema file
# If your file is named differently, adjust the import accordingly.
from db_schema import User, Product, Order, OrderItem, Base

# ---------------------------------------------------------------------------
# Setup engine and session
# ---------------------------------------------------------------------------

engine = create_engine("sqlite:///ecommerce.db", echo=True)
SessionLocal = sessionmaker(bind=engine)


def seed_data():
    """Insert some sample users, products, orders, and order_items."""
    session = SessionLocal()

    try:
        # -------------------------------------------------------------------
        # 1. Create Users
        # -------------------------------------------------------------------
        user1 = User(
            email="alice@example.com",
            password_hash="hashed_password_alice",
            full_name="Alice Smith",
            is_active=True,
            is_admin=False,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        user2 = User(
            email="bob@example.com",
            password_hash="hashed_password_bob",
            full_name="Bob Johnson",
            is_active=True,
            is_admin=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        session.add_all([user1, user2])

        # -------------------------------------------------------------------
        # 2. Create Products
        # -------------------------------------------------------------------
        product1 = Product(
            name="Wireless Mouse",
            description="Ergonomic wireless mouse with USB receiver",
            sku="WM-001",
            price=29.99,
            currency="USD",
            stock_quantity=100,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        product2 = Product(
            name="Mechanical Keyboard",
            description="Backlit mechanical keyboard with blue switches",
            sku="MK-001",
            price=79.99,
            currency="USD",
            stock_quantity=50,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        session.add_all([product1, product2])

        # Flush to assign IDs (without committing yet)
        session.flush()

        # -------------------------------------------------------------------
        # 3. Create an Order for Alice (user1)
        # -------------------------------------------------------------------
        order1 = Order(
            user_id=user1.id,          # link to Alice
            status="paid",
            total_amount=29.99 + 79.99,
            currency="USD",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
        )

        session.add(order1)
        session.flush()  # to get order1.id

        # -------------------------------------------------------------------
        # 4. Create OrderItems for that Order
        # -------------------------------------------------------------------
        order_item1 = OrderItem(
            order_id=order1.id,
            product_id=product1.id,
            quantity=1,
            unit_price=29.99,
            currency="USD",
        )

        order_item2 = OrderItem(
            order_id=order1.id,
            product_id=product2.id,
            quantity=1,
            unit_price=79.99,
            currency="USD",
        )

        session.add_all([order_item1, order_item2])

        # -------------------------------------------------------------------
        # Commit all changes
        # -------------------------------------------------------------------
        session.commit()
        print("Sample data inserted successfully.")

    except Exception as e:
        # Roll back in case of any error to avoid partial writes
        session.rollback()
        print(f"Error while inserting sample data: {e}")
    finally:
        # Always close the session
        session.close()


if __name__ == "__main__":
    seed_data()
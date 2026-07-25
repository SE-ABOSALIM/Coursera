"""
ecommerce_db.py

This module defines an e-commerce database schema and initializes it
in a local SQLite database using SQLAlchemy.

It models four core entities:
    - User:       Customers (and potentially admins)
    - Product:    Items available for purchase
    - Order:      A purchase transaction made by a user
    - OrderItem:  Individual line items within an order

Running this file directly (python ecommerce_db.py) will:
    - Connect to a SQLite database file named 'ecommerce.db'
    - Create the tables if they do not already exist
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------

from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean,
    DateTime, Numeric, ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# ---------------------------------------------------------------------------
# Engine & Base setup
# ---------------------------------------------------------------------------

# create_engine creates a SQLAlchemy Engine, which manages connections
# to the underlying database. Here we use SQLite with a local file
# named 'ecommerce.db'.
#
# The URL format 'sqlite:///ecommerce.db' means:
#   - sqlite:   use the SQLite dialect/driver
#   - ///      local filesystem path
#   - ecommerce.db: the database file name
#
# Note: echo=True tells SQLAlchemy to log all generated SQL to stdout,
# which is useful during development and debugging.
engine = create_engine("sqlite:///ecommerce.db", echo=False)

# declarative_base returns a base class for our ORM models.
# All model classes will inherit from this Base, and SQLAlchemy
# uses Base.metadata to keep track of tables and generate them.
Base = declarative_base()

# ---------------------------------------------------------------------------
# ORM Models (Schema)
# ---------------------------------------------------------------------------
# Each class below corresponds to a table in the database.
# Columns define the table fields, and relationships define
# how tables are linked to each other.
# ---------------------------------------------------------------------------


class User(Base):
    """
    Represents a user of the e-commerce platform.

    This can be a customer or an admin. A user can have multiple orders.
    """
    __tablename__ = "users"

    # Primary key (auto-incremented integer)
    id = Column(Integer, primary_key=True)

    # Unique email address for login/identification
    email = Column(String(255), unique=True, nullable=False)

    # Hashed password (never store plain text passwords!)
    password_hash = Column(String(255), nullable=False)

    # Full name of the user
    full_name = Column(String(255), nullable=False)

    # Flag indicating whether the user account is active
    is_active = Column(Boolean, default=True, nullable=False)

    # Flag indicating whether the user has admin privileges
    is_admin = Column(Boolean, default=False, nullable=False)

    # Timestamps for auditing and tracking
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship: one User -> many Orders
    # back_populates defines the reverse attribute on the Order model.
    orders = relationship("Order", back_populates="user")

    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email!r}>"


class Product(Base):
    """
    Represents a product in the catalog.

    Products can appear in many order items.
    """
    __tablename__ = "products"

    # Primary key (auto-incremented integer)
    id = Column(Integer, primary_key=True)

    # Product name
    name = Column(String(255), nullable=False)

    # Optional product description (longer text)
    description = Column(String, nullable=True)

    # Stock Keeping Unit (SKU), unique identifier for the product
    sku = Column(String(100), unique=True, nullable=False)

    # Current price of the product
    # Numeric(10, 2) means up to 10 digits total, 2 after the decimal.
    price = Column(Numeric(10, 2), nullable=False)

    # Currency code (e.g., "USD", "EUR")
    currency = Column(String(3), default="USD", nullable=False)

    # Quantity of this product currently in stock
    stock_quantity = Column(Integer, default=0, nullable=False)

    # Flag indicating whether the product is active (visible for sale)
    is_active = Column(Boolean, default=True, nullable=False)

    # Timestamps for auditing and tracking
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship: one Product -> many OrderItems
    order_items = relationship("OrderItem", back_populates="product")

    def __repr__(self) -> str:
        return f"<Product id={self.id} sku={self.sku!r} name={self.name!r}>"


class Order(Base):
    """
    Represents a single order placed by a user.

    An order can contain multiple order items.
    """
    __tablename__ = "orders"

    # Primary key (auto-incremented integer)
    id = Column(Integer, primary_key=True)

    # Foreign key referencing the user who placed the order
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Order status (e.g., "pending", "paid", "shipped", "cancelled")
    status = Column(String(50), default="pending", nullable=False)

    # Total monetary amount for the order
    total_amount = Column(Numeric(10, 2), nullable=False)

    # Currency code for the order total
    currency = Column(String(3), default="USD", nullable=False)

    # Timestamps for auditing and tracking
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationship: many Orders -> one User
    # This matches the 'orders' relationship defined on User.
    user = relationship("User", back_populates="orders")

    # Relationship: one Order -> many OrderItems
    items = relationship("OrderItem", back_populates="order")

    def __repr__(self) -> str:
        return f"<Order id={self.id} user_id={self.user_id} status={self.status!r}>"


class OrderItem(Base):
    """
    Represents a single line item within an order.

    Each OrderItem links an Order to a Product, with a quantity and price.
    """
    __tablename__ = "order_items"

    # Primary key (auto-incremented integer)
    id = Column(Integer, primary_key=True)

    # Foreign key referencing the parent order
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)

    # Foreign key referencing the product being purchased
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    # Quantity of the product in this line item
    quantity = Column(Integer, nullable=False)

    # Unit price at the time of purchase (can differ from current product price)
    unit_price = Column(Numeric(10, 2), nullable=False)

    # Currency code for the unit price
    currency = Column(String(3), default="USD", nullable=False)

    # Relationship: many OrderItems -> one Order
    order = relationship("Order", back_populates="items")

    # Relationship: many OrderItems -> one Product
    product = relationship("Product", back_populates="order_items")

    def __repr__(self) -> str:
        return (
            f"<OrderItem id={self.id} order_id={self.order_id} "
            f"product_id={self.product_id} quantity={self.quantity}>"
        )


# ---------------------------------------------------------------------------
# Database initialization and Session factory
# ---------------------------------------------------------------------------

def init_db() -> None:
    """
    Create all tables in the SQLite database if they do not exist.

    This function uses the metadata collected from all classes that inherit
    from Base (User, Product, Order, OrderItem) and issues the appropriate
    CREATE TABLE statements via the engine.
    """
    Base.metadata.create_all(engine)


# sessionmaker creates a factory for Session objects.
# A Session represents a transactional scope for interacting with the database:
#   - add / update / delete objects
#   - query the database
#
# Usage example:
#   session = SessionLocal()
#   user = User(email="test@example.com", ...)
#   session.add(user)
#   session.commit()
SessionLocal = sessionmaker(bind=engine)


# ---------------------------------------------------------------------------
# Script entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # When this file is run directly, initialize the database schema.
    init_db()
    print("Database initialized and tables created in ecommerce.db")
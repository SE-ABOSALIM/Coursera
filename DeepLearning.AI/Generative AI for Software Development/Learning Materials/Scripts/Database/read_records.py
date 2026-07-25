"""
view_ecommerce_data_simple.py

Script to query and display data from ecommerce.db in a simple,
terminal-friendly format.

It prints:
    - A title for each table
    - One line per record
"""

from sqlalchemy.orm import Session

# Import models and SessionLocal from your schema file
from db_schema import User, Product, Order, OrderItem, SessionLocal


def view_data():
    """Query and print users, products, orders, and order_items."""
    session: Session = SessionLocal()

    try:
        # -------------------------
        # USERS
        # -------------------------
        print("=== USERS ===")
        users = session.query(User).all()
        for u in users:
            print(f"{u.id} | {u.email} | {u.full_name} | is_admin={u.is_admin}")
        print()  # blank line after table

        # -------------------------
        # PRODUCTS
        # -------------------------
        print("=== PRODUCTS ===")
        products = session.query(Product).all()
        for p in products:
            print(
                f"{p.id} | {p.sku} | {p.name} | "
                f"price={p.price} {p.currency} | stock={p.stock_quantity}"
            )
        print()

        # -------------------------
        # ORDERS
        # -------------------------
        print("=== ORDERS ===")
        orders = session.query(Order).all()
        for o in orders:
            print(
                f"{o.id} | user_id={o.user_id} | status={o.status} | "
                f"total={o.total_amount} {o.currency}"
            )
        print()

        # -------------------------
        # ORDER_ITEMS
        # -------------------------
        print("=== ORDER_ITEMS ===")
        order_items = session.query(OrderItem).all()
        for oi in order_items:
            print(
                f"{oi.id} | order_id={oi.order_id} | product_id={oi.product_id} | "
                f"quantity={oi.quantity} | unit_price={oi.unit_price} {oi.currency}"
            )
        print()

    finally:
        session.close()


if __name__ == "__main__":
    view_data()
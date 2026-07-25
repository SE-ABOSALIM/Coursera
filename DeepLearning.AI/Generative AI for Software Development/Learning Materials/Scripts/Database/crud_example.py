"""
crud_example.py

Demonstrates basic CRUD operations on the ecommerce.db database:
    - Create: insert new User and Product records
    - Read:   fetch and display records
    - Update: modify existing records
    - Delete: remove records

Assumes:
    - ecommerce_db.py is in the same directory
    - ecommerce_db.py defines: User, Product, SessionLocal
"""

from datetime import datetime
from sqlalchemy.orm import Session

from db_schema import User, Product, SessionLocal


def create_user(session: Session, email: str, password_hash: str, full_name: str) -> User:
    """Create and persist a new User."""
    user = User(
        email=email,
        password_hash=password_hash,
        full_name=full_name,
        is_active=True,
        is_admin=False,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(user)
    session.commit()
    session.refresh(user)  # reload from DB to get the assigned ID
    return user


def create_product(session: Session, name: str, sku: str, price: float) -> Product:
    """Create and persist a new Product."""
    product = Product(
        name=name,
        description=None,
        sku=sku,
        price=price,
        currency="USD",
        stock_quantity=10,
        is_active=True,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def read_users(session: Session):
    """Read and print all users."""
    users = session.query(User).all()
    print("=== USERS ===")
    for u in users:
        print(f"{u.id} | {u.email} | {u.full_name} | is_admin={u.is_admin}")
    print()


def read_products(session: Session):
    """Read and print all products."""
    products = session.query(Product).all()
    print("=== PRODUCTS ===")
    for p in products:
        print(f"{p.id} | {p.sku} | {p.name} | price={p.price} {p.currency}")
    print()


def update_user_name(session: Session, user_id: int, new_name: str):
    """Update the full_name of a User."""
    user = session.get(User, user_id)
    if not user:
        print(f"User with id={user_id} not found.")
        return

    user.full_name = new_name
    user.updated_at = datetime.utcnow()
    session.commit()
    print(f"Updated user {user_id} name to {new_name}")


def update_product_price(session: Session, product_id: int, new_price: float):
    """Update the price of a Product."""
    product = session.get(Product, product_id)
    if not product:
        print(f"Product with id={product_id} not found.")
        return

    product.price = new_price
    product.updated_at = datetime.utcnow()
    session.commit()
    print(f"Updated product {product_id} price to {new_price}")


def delete_user(session: Session, user_id: int):
    """Delete a User by id."""
    user = session.get(User, user_id)
    if not user:
        print(f"User with id={user_id} not found.")
        return

    session.delete(user)
    session.commit()
    print(f"Deleted user {user_id}")


def delete_product(session: Session, product_id: int):
    """Delete a Product by id."""
    product = session.get(Product, product_id)
    if not product:
        print(f"Product with id={product_id} not found.")
        return

    session.delete(product)
    session.commit()
    print(f"Deleted product {product_id}")


def main():
    # Open a session
    session = SessionLocal()

    try:
        # ----------------- CREATE -----------------
        print("Creating sample user and product...")
        user = create_user(
            session,
            email="charlie@example.com",
            password_hash="hashed_password_charlie",
            full_name="Charlie Brown",
        )
        product = create_product(
            session,
            name="USB-C Charger",
            sku="UC-001",
            price=19.99,
        )

        # ----------------- READ -------------------
        read_users(session)
        read_products(session)

        # ----------------- UPDATE -----------------
        print("Updating records...")
        update_user_name(session, user_id=user.id, new_name="Charles Brown")
        update_product_price(session, product_id=product.id, new_price=24.99)

        # Show updated data
        read_users(session)
        read_products(session)

        # ----------------- DELETE -----------------
        print("Deleting records...")
        delete_user(session, user_id=user.id)
        delete_product(session, product_id=product.id)

        # Show remaining data
        read_users(session)
        read_products(session)

    finally:
        session.close()


if __name__ == "__main__":
    main()
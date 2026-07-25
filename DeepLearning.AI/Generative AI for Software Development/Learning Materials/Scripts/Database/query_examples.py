from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker, Session

from db_schema import Order, Product, OrderItem

engine = create_engine("sqlite:///ecommerce.db", echo=False)
SessionLocal = sessionmaker(bind=engine)

def get_orders_for_user(user_id: int):
    session: Session = SessionLocal()
    try:
        orders = (
            session.query(Order)
            .filter(Order.user_id == user_id)
            .all()
        )
        return orders
    finally:
        session.close()

def get_total_quantity_sold_per_product():
    session: Session = SessionLocal()
    try:
        # Aggregate quantity per product_id, joined with Product for name/sku
        results = (
            session.query(
                Product.id,
                Product.sku,
                Product.name,
                func.coalesce(func.sum(OrderItem.quantity), 0).label("total_quantity_sold"),
            )
            .join(OrderItem, OrderItem.product_id == Product.id)
            .group_by(Product.id, Product.sku, Product.name)
            .all()
        )

        return results
    finally:
        session.close()

if __name__ == "__main__":
    print("\n=== ORDERS PLACED BY A SPECIFIC USER ===")
    user_id = 1
    orders = get_orders_for_user(user_id)
    for o in orders:
        print(f"Order ID={o.id}, status={o.status}, total={o.total_amount} {o.currency}")

    totals = get_total_quantity_sold_per_product()
    print("\n=== TOTAL QUANTITY SOLD PER PRODUCT ===")
    for product_id, sku, name, total_qty in totals:
        print(f"Product ID={product_id} | SKU={sku} | Name={name} | Total Sold={total_qty}")
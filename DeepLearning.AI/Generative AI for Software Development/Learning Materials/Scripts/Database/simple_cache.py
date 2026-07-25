"""
cache_products.py

Demonstrates simple caching of a "get all products" query using
Dogpile caching, and compares execution time before and after caching.

Requirements:
    pip install dogpile.cache

Assumptions:
    - ecommerce_db.py exists in the same directory
    - ecommerce_db.py defines: Product, SessionLocal
    - You have already inserted many products (e.g., 1000) into the DB
"""

import time

from dogpile.cache import make_region
from sqlalchemy.orm import Session

from db_schema import Product, SessionLocal

# ---------------------------------------------------------------------------
# Dogpile cache configuration
# ---------------------------------------------------------------------------

# Using a simple in-memory cache backend for demonstration.
# In a real app you might use 'dogpile.cache.redis' or 'dogpile.cache.memcached'.
region = make_region().configure(
    "dogpile.cache.memory",
    expiration_time=60,  # seconds; cached data lives for 1 minute
)


# ---------------------------------------------------------------------------
# Cached function
# ---------------------------------------------------------------------------

@region.cache_on_arguments()
def get_all_products():
    """
    Retrieve all products from the database.

    Because of @cache_on_arguments, the result of this function call
    will be cached based on its arguments (here: none), so subsequent
    calls within the expiration_time will return the cached result
    instead of hitting the database again.
    """
    # We open a new session each time; Dogpile will cache the *result*.
    session: Session = SessionLocal()
    try:
        products = session.query(Product).all()
        return products
    finally:
        session.close()


# ---------------------------------------------------------------------------
# Timing helper
# ---------------------------------------------------------------------------

def timed_call(func, *args, **kwargs):
    """
    Call `func` with given args/kwargs and return (result, elapsed_seconds).
    """
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    elapsed = end - start
    return result, elapsed


# ---------------------------------------------------------------------------
# Main test
# ---------------------------------------------------------------------------

def main():
    # First call: should hit the database and then cache the result.
    products_1, elapsed_1 = timed_call(get_all_products)
    print(f"First call: retrieved {len(products_1)} products in {elapsed_1:.6f} seconds")

    # Second call: should be served from cache (much faster).
    products_2, elapsed_2 = timed_call(get_all_products)
    print(f"Second call (cached): retrieved {len(products_2)} products in {elapsed_2:.6f} seconds")

    # Sanity check: both lists should be the same length
    assert len(products_1) == len(products_2)


if __name__ == "__main__":
    main()
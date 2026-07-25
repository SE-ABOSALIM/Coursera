from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('sqlite:///ecommerce.db', echo=True)

def is_sqlite_live(engine) -> bool:
    """
    Returns True if the SQLite database is accessible and a simple
    query can be executed via SQLAlchemy, False otherwise.
    """
    try:
        # Get a connection from the engine
        with engine.connect() as conn:
            # Run a trivial query
            result = conn.execute(text("SELECT 1"))
            _ = result.scalar()  # fetch the single value
        return True
    except SQLAlchemyError as e:
        # Optional: log or print the error
        # print(f"Database error: {e}")
        return False

if __name__ == "__main__":
    if is_sqlite_live(engine):
        print("SQLite database is live and accessible via SQLAlchemy.")
    else:
        print("SQLite database is NOT accessible via SQLAlchemy.")
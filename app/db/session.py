import logging
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from app.core.config import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the engine and connect to the database
try:
    engine = create_engine(settings.DB)
    logger.info("Accessed the database engine.")

except SQLAlchemyError as e:
    logger.error(f"Failed to connect to the database. Error: {e}")
    raise e  # Re-raise the exception if you want to stop execution

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

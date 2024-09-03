from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def init_models():
    from app.models.item import Item
    from app.models.user import User
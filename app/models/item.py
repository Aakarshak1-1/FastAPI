from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)

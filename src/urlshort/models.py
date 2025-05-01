from sqlalchemy import Column, Integer, String
from src.database import Base


class Urls(Base):
    __tablename__ = 'urls'
    short_url = Column(String, primary_key=True, index=True)
    original_url = Column(String)

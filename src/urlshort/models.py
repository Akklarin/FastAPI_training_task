from sqlalchemy import Column, Integer, String
from src.database import Base


class Urls(Base):
    __tablename__ = 'urls'
    id = Column(Integer, primary_key=True, index=True)
    short_url = Column(String, unique=True)
    original_url = Column(String, nullable=False)

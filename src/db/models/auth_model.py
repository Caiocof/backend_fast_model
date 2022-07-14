from sqlalchemy import Column, Integer, String

from src.db.settings.config import Base


class AuthModel(Base):
    __tablename__ = "auth"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

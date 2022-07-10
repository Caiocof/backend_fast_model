from sqlalchemy import Column, Integer, String

from src.db.settings.config import Base


class ExampleModel(Base):
    __tablename__ = "example_model"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)

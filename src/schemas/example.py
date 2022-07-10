from typing import Optional
from pydantic.dataclasses import dataclass


@dataclass
class ExampleBase:
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

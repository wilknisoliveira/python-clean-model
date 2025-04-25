from domain.entity import Entity
from sqlalchemy import Column, String
from .base import Base


class User(Entity, Base):
    __tablename__ = 'users'
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, name: str, email: str, password: str):
        super().__init__()
        self.name: str = name
        self.email: str = email
        self.password: str = password

    # Use Rich Entity approach, keeping all the business logic inside the Domain Layer.



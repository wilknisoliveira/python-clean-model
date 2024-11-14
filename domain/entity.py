import datetime
from sqlalchemy import Column, Integer, DateTime


class Entity:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self):
        self.created_at: datetime = datetime.UTC
        self.updated_at: datetime = datetime.UTC

import datetime
from sqlalchemy import Column, Integer, DateTime


class Entity:
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    def __init__(self):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.created_at: datetime = now
        self.updated_at: datetime = now

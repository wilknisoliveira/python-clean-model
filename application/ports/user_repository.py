from abc import ABC, abstractmethod
from domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: User):
        pass

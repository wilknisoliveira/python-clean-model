from application.ports.user_repository import UserRepository
from domain.user import User


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository: UserRepository = user_repository

    def execute(self, name: str, email: str, password: str):
        user = User(name, email, password)

        result = self.user_repository.create(user)
        return "User Created"




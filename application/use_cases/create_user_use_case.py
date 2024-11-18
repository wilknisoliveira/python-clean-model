from application.ports.user_repository import UserRepository
from domain.user import User
import inject
from .dtos.user_dto_response import UserDtoResponse


class CreateUserUseCase:
    @inject.autoparams()
    def __init__(self, user_repository: UserRepository):
        self.user_repository: UserRepository = user_repository

    def execute(self, name: str, email: str, password: str) -> UserDtoResponse:
        user = User(name, email, password)

        response = UserDtoResponse(
            user.name,
            user.email
        )

        self.user_repository.create(user)
        return response




from sqlalchemy import String


class UserDtoResponse:
    name: str
    email: str

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
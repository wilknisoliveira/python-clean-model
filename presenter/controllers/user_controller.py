from presenter import presenter
from flask import request

# Controllers
from application.use_cases.create_user_use_case import CreateUserUseCase

route_base = '/users'


@presenter.route(f'{route_base}', methods=['POST'])
def create():
    name: str = request.form.get('name')
    email: str = request.form.get('email')
    password: str = request.form.get('password')

    create_user_use_case = CreateUserUseCase()

    result = create_user_use_case.execute(name, email, password)

    return result


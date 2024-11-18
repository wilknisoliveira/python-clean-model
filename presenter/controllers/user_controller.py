from presenter import presenter
from flask import request, jsonify
from infra.persistance.repositories.user_repository_db import UserRepositoryDb

# Controllers
from application.use_cases.create_user_use_case import CreateUserUseCase

route_base = '/users'


@presenter.route(f'{route_base}', methods=['POST'])
def create():
    data = request.json
    if not data:
        return jsonify({
            "error": "Invalid JSON Format"
        }), 400

    name: str = data.get('name')
    email: str = data.get('email')
    password: str = data.get('password')
    user_repository_db = UserRepositoryDb()
    create_user_use_case = CreateUserUseCase(user_repository_db)

    result = create_user_use_case.execute(name, email, password)

    return result


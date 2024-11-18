import inject
from application.ports.user_repository import UserRepository
from infra.persistance.repositories.user_repository_db import UserRepositoryDb


def ioc_config(binder):
    binder.bind(UserRepository, UserRepositoryDb())

def register_ioc():
    inject.configure(ioc_config)
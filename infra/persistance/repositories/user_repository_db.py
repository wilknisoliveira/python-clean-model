from application.ports.user_repository import UserRepository
from domain.user import User
from infra.persistance.db_connection_handler import DBConnectionHandler
from sqlalchemy.orm.exc import NoResultFound


class UserRepositoryDb(UserRepository):
    def create(self, user: User):
        with DBConnectionHandler() as db:
            try:
                db.session.add(user)
                db.session.commit()
            except Exception as ex:
                db.session.rollback()
                raise ex

    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                result = db.session.query(User).all()
                return result
            except NoResultFound:
                return None

    def update(self, user: User):
        try:
            with DBConnectionHandler() as db:
                db.session.update(user)
                db.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise ex

    def delete(self, id: int):
        try:
            with DBConnectionHandler() as db:
                db.session.query(User).filter(User.id == id).delete()
                db.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise ex

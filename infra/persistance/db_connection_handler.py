from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self):
        load_dotenv()
        database_strings = os.getenv('DATABASE_STRINGS')
        self.__connection_string = f'mysql+pymysql://{database_strings}'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()





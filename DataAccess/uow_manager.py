
from .uow import UOW

import sqlite3


class UOWManager:
    def __init__(self):
        self.__db_connection = sqlite3.connect('./Data/playlist.db')

    def __enter__(self):
        cursor = self.__db_connection.cursor()
        cursor.row_factory = sqlite3.Row
        return UOW(cursor)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_value:
            self.__db_connection.rollback()
        else:
            self.__db_connection.commit()

        self.__db_connection.close()

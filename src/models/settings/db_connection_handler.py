import sqlite3
from sqlite3 import Connection

class __DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_str = "storage.db"
        self._conn = None

    def connect(self) -> None:
        self._conn = sqlite3.connect(self.__connection_str)

    def get_connection(self) -> Connection:
        return self._conn
    

db_connection_handler = __DBConnectionHandler()
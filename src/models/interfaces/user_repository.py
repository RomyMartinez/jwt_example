from sqlite3 import Connection
from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):
    @abstractmethod
    def __init__(self, conn: Connection) -> None:
        pass

    @abstractmethod
    def registry_user(self, username: str, password: str) -> None:
        pass

    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> tuple:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass
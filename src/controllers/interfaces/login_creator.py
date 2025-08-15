from abc import ABC, abstractmethod
from src.models.interfaces.user_repository import UserRepositoryInterface
from typing import Dict

class LoginCreatorInterface(ABC):
    @abstractmethod
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        pass

    @abstractmethod
    def create_login(self, username: str, password: str) -> Dict:
        pass
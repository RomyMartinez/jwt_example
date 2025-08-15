from abc import ABC, abstractmethod
from src.models.interfaces.user_repository import UserRepositoryInterface
from typing import Dict

class BalanceEditorInterface(ABC):
    @abstractmethod
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        pass

    @abstractmethod
    def edit_balance(self, user_id: str, new_balance: float) -> Dict:
        pass
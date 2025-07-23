from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler

def test_repository():
    db_connection_handler.connect()
    conn = db_connection_handler.get_connection()
    user_repo = UserRepository(conn)

    username = "Erwin"
    passord = "123456"

    user = user_repo.get_user_by_username(username)

from src.drivers.passord_handler import PasswordHandler

def test_encrypt_password():
    password = "123456"
    password_handler = PasswordHandler()
    hashed_password = password_handler.encrypt_password(password)
    assert hashed_password != password

def test_check_password():
    password = "123456"
    password_handler = PasswordHandler()
    hashed_password = password_handler.encrypt_password(password)
    isCheck = PasswordHandler().check_password(password, hashed_password)
    assert isCheck
import jwt
from datetime import datetime, timedelta, timezone
from src.configs.jwt_configs import jwt_infos

class JwtHandler:
    def create_jwt_token(self, body: dict = {}) -> str:
       token = jwt.encode(
                payload={
                    "exp": datetime.now(timezone.utc) + timedelta(hours=jwt_infos["JWT_HOURS"]),
                    **body,
                },
                key=jwt_infos["KEY"],
                algorithm=jwt_infos["ALGORITHM"],
            )   
       return token
    
    def decode_jwt_token(self, token: str) -> dict:
        token_info = jwt.decode(token, key="secret", algorithms="HS256")
        return token_info
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError

from config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_HOURS


def crear_token(usuario_id: int, rol: str, rol_id: int = None) -> str:
    payload = {
        "sub": str(usuario_id),
        "rol": rol,
        "rol_id": rol_id,
        "exp": datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRATION_HOURS),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def verificar_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from auth.jwt_handler import verificar_token

bearer_scheme = HTTPBearer(auto_error=False)


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
) -> dict:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"ok": False, "error": "Token requerido"},
        )
    payload = verificar_token(credentials.credentials)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"ok": False, "error": "Token inválido o expirado"},
        )
    return {
        "id": int(payload["sub"]),
        "rol": payload["rol"],
        "rol_id": payload.get("rol_id"),
    }


def require_roles(roles: list[str]):
    async def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user["rol"] not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"ok": False, "error": "No autorizado"},
            )
        return current_user
    return role_checker

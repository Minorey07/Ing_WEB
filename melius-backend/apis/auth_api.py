from fastapi import APIRouter, Depends

from esquema.usuario import Usuario
from esquema.auth_schemas import LoginRequest
from auth.jwt_handler import crear_token
from auth.dependencies import get_current_user
from servicios import usuario_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(req: LoginRequest):
    user = usuario_service.verificar_login(req.correo, req.password)
    if not user:
        return {"ok": False, "error": "Credenciales inválidas"}
    token = crear_token(user["id"], user["rol"])
    return {
        "ok": True,
        "data": {
            "token": token,
            "usuario": {
                "id": user["id"],
                "nombre": user["nombre"],
                "correo": user["correo"],
                "rol": user["rol"],
            },
        },
    }


@router.get("/me")
def me(current_user: dict = Depends(get_current_user)):
    usuarios = usuario_service.listar()
    user = next((u for u in usuarios if u["id"] == current_user["id"]), None)
    if not user:
        return {"ok": False, "error": "Usuario no encontrado"}
    return {
        "ok": True,
        "data": {
            "id": user["id"],
            "nombre": user["nombre"],
            "correo": user["correo"],
            "rol": user["rol"],
        },
    }

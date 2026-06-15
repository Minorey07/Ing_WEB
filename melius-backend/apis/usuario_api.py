from fastapi import APIRouter
from esquema.usuario import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

usuarios = [
    Usuario(id=1, nombre="Admin", rol="ADMIN", password="123")
]

@router.post("/login")
def login(user: Usuario):
    for u in usuarios:
        if u.nombre == user.nombre and u.password == user.password:
            return {"ok": True, "usuario": u}
    return {"ok": False}
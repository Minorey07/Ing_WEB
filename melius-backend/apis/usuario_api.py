from fastapi import APIRouter, Depends

from esquema.usuario import Usuario
from auth.dependencies import get_current_user, require_roles
from servicios import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("/")
def listar(current_user: dict = Depends(require_roles(["ADMIN"]))):
    data = usuario_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(u: Usuario, current_user: dict = Depends(require_roles(["ADMIN"]))):
    data = usuario_service.crear(u)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, u: Usuario, current_user: dict = Depends(require_roles(["ADMIN"]))):
    u.id = id
    data = usuario_service.actualizar(u)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(require_roles(["ADMIN"]))):
    usuario_service.eliminar(id)
    return {"ok": True, "data": None}

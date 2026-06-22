from fastapi import APIRouter, Depends

from esquema.categoria import Categoria
from auth.dependencies import get_current_user, require_roles
from repositorio import categoria_repository

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = categoria_repository.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(p: Categoria, current_user: dict = Depends(require_roles(["ADMIN", "ALMACENERO"]))):
    data = categoria_repository.crear(p)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, p: Categoria, current_user: dict = Depends(require_roles(["ADMIN", "ALMACENERO"]))):
    p.id = id
    data = categoria_repository.actualizar(p)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(require_roles(["ADMIN"]))):
    categoria_repository.eliminar(id)
    return {"ok": True, "data": None}

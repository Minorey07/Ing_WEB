from fastapi import APIRouter, Depends

from esquema.cliente import Cliente
from auth.dependencies import get_current_user
from servicios import cliente_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = cliente_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(c: Cliente, current_user: dict = Depends(get_current_user)):
    data = cliente_service.crear(c)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, c: Cliente, current_user: dict = Depends(get_current_user)):
    c.id = id
    data = cliente_service.actualizar(c)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(get_current_user)):
    cliente_service.eliminar(id)
    return {"ok": True, "data": None}

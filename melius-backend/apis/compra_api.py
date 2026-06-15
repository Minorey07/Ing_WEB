from fastapi import APIRouter, Depends

from esquema.compra import Compra
from auth.dependencies import get_current_user
from servicios import compra_service

router = APIRouter(prefix="/compras", tags=["Compras"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = compra_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(c: Compra, current_user: dict = Depends(get_current_user)):
    data = compra_service.crear(c)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, c: Compra, current_user: dict = Depends(get_current_user)):
    c.id = id
    data = compra_service.actualizar(c)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(get_current_user)):
    compra_service.eliminar(id)
    return {"ok": True, "data": None}

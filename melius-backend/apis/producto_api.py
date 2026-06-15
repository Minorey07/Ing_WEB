from fastapi import APIRouter, Depends

from esquema.producto import Producto
from auth.dependencies import get_current_user
from servicios import producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = producto_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(p: Producto, current_user: dict = Depends(get_current_user)):
    data = producto_service.crear(p)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, p: Producto, current_user: dict = Depends(get_current_user)):
    p.id = id
    data = producto_service.actualizar(p)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(get_current_user)):
    producto_service.eliminar(id)
    return {"ok": True, "data": None}

from fastapi import APIRouter, Depends

from esquema.proveedor import Proveedor
from auth.dependencies import get_current_user
from servicios import proveedor_service

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = proveedor_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(p: Proveedor, current_user: dict = Depends(get_current_user)):
    data = proveedor_service.crear(p)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, p: Proveedor, current_user: dict = Depends(get_current_user)):
    p.id = id
    data = proveedor_service.actualizar(p)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(get_current_user)):
    proveedor_service.eliminar(id)
    return {"ok": True, "data": None}

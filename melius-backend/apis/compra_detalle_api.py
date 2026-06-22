from fastapi import APIRouter, Depends

from esquema.compra_detalle import CompraDetalle
from auth.dependencies import get_current_user
from servicios import compra_detalle_service

router = APIRouter(prefix="/compra-detalles", tags=["Compra Detalles"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = compra_detalle_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(d: CompraDetalle, current_user: dict = Depends(get_current_user)):
    data = compra_detalle_service.crear(d.model_dump(exclude={"id", "producto_nombre"}))
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(get_current_user)):
    compra_detalle_service.eliminar(id)
    return {"ok": True, "data": None}
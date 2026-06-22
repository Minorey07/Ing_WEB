from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from esquema.pedido import Pedido
from auth.dependencies import get_current_user
from servicios import pedido_service

class CambioEstado(BaseModel):
    estado_id: int

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = pedido_service.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(p: Pedido, current_user: dict = Depends(get_current_user)):
    try:
        data = pedido_service.crear(p)
        return {"ok": True, "data": data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail={"ok": False, "error": str(e)})


@router.put("/{id}")
def actualizar(id: int, p: Pedido, current_user: dict = Depends(get_current_user)):
    p.id = id
    rol_id = current_user.get("rol_id")
    data = pedido_service.actualizar(p, rol_id)
    return {"ok": True, "data": data}


@router.put("/{id}/estado")
def actualizar_estado(id: int, body: CambioEstado, current_user: dict = Depends(get_current_user)):
    rol_id = current_user.get("rol_id")
    data = pedido_service.actualizar_solo_estado(id, body.estado_id, rol_id)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(get_current_user)):
    pedido_service.eliminar(id)
    return {"ok": True, "data": None}

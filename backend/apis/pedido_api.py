from fastapi import APIRouter, HTTPException
from esquema.pedido import Pedido
from servicios import pedido_service

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/")
def listar():
    """Obtiene todos los pedidos"""
    return pedido_service.listar()

@router.get("/{id}")
def obtener(id: int):
    """Obtiene un pedido por ID"""
    pedido = pedido_service.obtener_por_id(id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedido

@router.post("/")
def crear(p: Pedido):
    """Crea un nuevo pedido"""
    try:
        return pedido_service.crear(p)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{id}")
def actualizar(id: int, p: Pedido):
    """Actualiza un pedido"""
    p.id = id
    resultado = pedido_service.actualizar(p)
    if not resultado:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar(id: int):
    """Elimina un pedido"""
    pedido = pedido_service.obtener_por_id(id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    pedido_service.eliminar(id)
    return {"mensaje": "Pedido eliminado exitosamente"}
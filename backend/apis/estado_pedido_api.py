from fastapi import APIRouter, HTTPException
from esquema.estado_pedido import EstadoPedido
from servicios import estado_pedido_service

router = APIRouter(prefix="/estados-pedido", tags=["Estados de Pedido"])

@router.get("/")
def obtener_todos_estados():
    """Obtiene todos los estados de pedido"""
    return estado_pedido_service.listar()

@router.get("/{id}")
def obtener_estado(id: int):
    """Obtiene un estado por ID"""
    estado = estado_pedido_service.obtener_por_id(id)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado

@router.post("/")
def crear_estado(estado: EstadoPedido):
    """Crea un nuevo estado"""
    return estado_pedido_service.crear(estado)

@router.put("/{id}")
def actualizar_estado(id: int, estado: EstadoPedido):
    """Actualiza un estado"""
    estado.id = id
    resultado = estado_pedido_service.actualizar(estado)
    if not resultado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar_estado(id: int):
    """Elimina un estado"""
    estado = estado_pedido_service.obtener_por_id(id)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    estado_pedido_service.eliminar(id)
    return {"mensaje": "Estado eliminado exitosamente"}


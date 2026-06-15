from fastapi import APIRouter, HTTPException
from esquema.estado_producto import EstadoProducto
from servicios import estado_producto_service

router = APIRouter(prefix="/estados-producto", tags=["Estados de Producto"])

@router.get("/")
def obtener_todos_estados():
    """Obtiene todos los estados de producto"""
    return estado_producto_service.listar()

@router.get("/{id}")
def obtener_estado(id: int):
    """Obtiene un estado por ID"""
    estado = estado_producto_service.obtener_por_id(id)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return estado

@router.post("/")
def crear_estado(estado: EstadoProducto):
    """Crea un nuevo estado"""
    return estado_producto_service.crear(estado)

@router.put("/{id}")
def actualizar_estado(id: int, estado: EstadoProducto):
    """Actualiza un estado"""
    estado.id = id
    resultado = estado_producto_service.actualizar(estado)
    if not resultado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar_estado(id: int):
    """Elimina un estado"""
    estado = estado_producto_service.obtener_por_id(id)
    if not estado:
        raise HTTPException(status_code=404, detail="Estado no encontrado")
    estado_producto_service.eliminar(id)
    return {"mensaje": "Estado eliminado exitosamente"}


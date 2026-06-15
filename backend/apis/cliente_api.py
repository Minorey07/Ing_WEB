from fastapi import APIRouter, HTTPException
from esquema.cliente import Cliente
from servicios import cliente_service

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/")
def listar():
    """Obtiene todos los clientes"""
    return cliente_service.listar()

@router.get("/{id}")
def obtener(id: int):
    """Obtiene un cliente por ID"""
    cliente = cliente_service.obtener_por_id(id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/")
def crear(c: Cliente):
    """Crea un nuevo cliente"""
    return cliente_service.crear(c)

@router.put("/{id}")
def actualizar(id: int, c: Cliente):
    """Actualiza un cliente"""
    c.id = id
    resultado = cliente_service.actualizar(c)
    if not resultado:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar(id: int):
    """Elimina un cliente"""
    cliente = cliente_service.obtener_por_id(id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    cliente_service.eliminar(id)
    return {"mensaje": "Cliente eliminado exitosamente"}
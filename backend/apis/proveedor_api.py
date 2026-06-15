from fastapi import APIRouter, HTTPException
from esquema.proveedor import Proveedor
from servicios import proveedor_service

router = APIRouter(prefix="/proveedores", tags=["Proveedores"])

@router.get("/")
def listar():
    """Obtiene todos los proveedores"""
    return proveedor_service.listar()

@router.get("/{id}")
def obtener(id: int):
    """Obtiene un proveedor por ID"""
    proveedor = proveedor_service.obtener_por_id(id)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

@router.post("/")
def crear(p: Proveedor):
    """Crea un nuevo proveedor"""
    return proveedor_service.crear(p)

@router.put("/{id}")
def actualizar(id: int, p: Proveedor):
    """Actualiza un proveedor"""
    p.id = id
    resultado = proveedor_service.actualizar(p)
    if not resultado:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar(id: int):
    """Elimina un proveedor"""
    proveedor = proveedor_service.obtener_por_id(id)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    proveedor_service.eliminar(id)
    return {"mensaje": "Proveedor eliminado exitosamente"}

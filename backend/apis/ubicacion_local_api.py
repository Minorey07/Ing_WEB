from fastapi import APIRouter, HTTPException
from esquema.ubicacion_local import UbicacionLocal
from servicios import ubicacion_local_service

router = APIRouter(prefix="/ubicaciones-locales", tags=["Ubicaciones Locales"])

@router.get("/")
def obtener_todas_ubicaciones():
    """Obtiene todas las ubicaciones locales"""
    return ubicacion_local_service.listar()

@router.get("/{id}")
def obtener_ubicacion(id: int):
    """Obtiene una ubicación por ID"""
    ubicacion = ubicacion_local_service.obtener_por_id(id)
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return ubicacion

@router.post("/")
def crear_ubicacion(ubicacion: UbicacionLocal):
    """Crea una nueva ubicación"""
    return ubicacion_local_service.crear(ubicacion)

@router.put("/{id}")
def actualizar_ubicacion(id: int, ubicacion: UbicacionLocal):
    """Actualiza una ubicación"""
    ubicacion.id = id
    resultado = ubicacion_local_service.actualizar(ubicacion)
    if not resultado:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return resultado

@router.delete("/{id}")
def eliminar_ubicacion(id: int):
    """Elimina una ubicación"""
    ubicacion = ubicacion_local_service.obtener_por_id(id)
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    ubicacion_local_service.eliminar(id)
    return {"mensaje": "Ubicación eliminada exitosamente"}


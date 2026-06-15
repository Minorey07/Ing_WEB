from fastapi import APIRouter, HTTPException
from esquema.ubicacion_nacional import UbicacionNacional
from servicios import ubicacion_nacional_service

router = APIRouter(prefix="/ubicaciones-nacionales", tags=["Ubicaciones Nacionales"])

@router.get("/")
def obtener_todas_ubicaciones():
    """Obtiene todas las ubicaciones nacionales"""
    return ubicacion_nacional_service.listar()

@router.get("/{id}")
def obtener_ubicacion(id: int):
    """Obtiene una ubicación por ID"""
    ubicacion = ubicacion_nacional_service.obtener_por_id(id)
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return ubicacion

@router.post("/")
def crear_ubicacion(ubicacion: UbicacionNacional):
    """Crea una nueva ubicación"""
    return ubicacion_nacional_service.crear(ubicacion)

@router.put("/{id}")
def actualizar_ubicacion(id: int, ubicacion: UbicacionNacional):
    """Actualiza una ubicación"""
    ubicacion.id = id
    resultado = ubicacion_nacional_service.actualizar(ubicacion)
    if not resultado:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return resultado

@router.delete("/{id}")
def eliminar_ubicacion(id: int):
    """Elimina una ubicación"""
    ubicacion = ubicacion_nacional_service.obtener_por_id(id)
    if not ubicacion:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    ubicacion_nacional_service.eliminar(id)
    return {"mensaje": "Ubicación eliminada exitosamente"}

    return {"mensaje": "Ubicación eliminada exitosamente"}

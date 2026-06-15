from repositorio import ubicacion_local_repository
from esquema.ubicacion_local import UbicacionLocal

def listar():
    """Lista todas las ubicaciones locales"""
    return ubicacion_local_repository.listar()

def obtener_por_id(id: int):
    """Obtiene una ubicación por ID"""
    return ubicacion_local_repository.obtener_por_id(id)

def obtener_por_distrito(distrito: str):
    """Obtiene ubicaciones por distrito"""
    return ubicacion_local_repository.obtener_por_distrito(distrito)

def crear(ubicacion: UbicacionLocal):
    """Crea una nueva ubicación"""
    return ubicacion_local_repository.crear(ubicacion)

def actualizar(ubicacion: UbicacionLocal):
    """Actualiza una ubicación"""
    return ubicacion_local_repository.actualizar(ubicacion)

def eliminar(id: int):
    """Elimina una ubicación"""
    ubicacion_local_repository.eliminar(id)

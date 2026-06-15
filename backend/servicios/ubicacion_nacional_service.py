from repositorio import ubicacion_nacional_repository
from esquema.ubicacion_nacional import UbicacionNacional

def listar():
    """Lista todas las ubicaciones nacionales"""
    return ubicacion_nacional_repository.listar()

def obtener_por_id(id: int):
    """Obtiene una ubicación por ID"""
    return ubicacion_nacional_repository.obtener_por_id(id)

def obtener_por_ciudad(ciudad: str):
    """Obtiene ubicaciones por ciudad"""
    return ubicacion_nacional_repository.obtener_por_ciudad(ciudad)

def obtener_por_departamento(departamento: str):
    """Obtiene ubicaciones por departamento"""
    return ubicacion_nacional_repository.obtener_por_departamento(departamento)

def crear(ubicacion: UbicacionNacional):
    """Crea una nueva ubicación"""
    return ubicacion_nacional_repository.crear(ubicacion)

def actualizar(ubicacion: UbicacionNacional):
    """Actualiza una ubicación"""
    return ubicacion_nacional_repository.actualizar(ubicacion)

def eliminar(id: int):
    """Elimina una ubicación"""
    ubicacion_nacional_repository.eliminar(id)

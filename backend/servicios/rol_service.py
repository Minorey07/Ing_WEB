from repositorio import rol_repository
from esquema.rol import Rol

def listar():
    """Lista todos los roles"""
    return rol_repository.listar()

def obtener_por_id(id: int):
    """Obtiene un rol por ID"""
    return rol_repository.obtener_por_id(id)

def obtener_por_nombre(nombre: str):
    """Obtiene un rol por nombre"""
    return rol_repository.obtener_por_nombre(nombre)

def crear(rol: Rol):
    """Crea un nuevo rol"""
    return rol_repository.crear(rol)

def actualizar(rol: Rol):
    """Actualiza un rol"""
    return rol_repository.actualizar(rol)

def eliminar(id: int):
    """Elimina un rol"""
    rol_repository.eliminar(id)

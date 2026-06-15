from repositorio import estado_producto_repository
from esquema.estado_producto import EstadoProducto

def listar():
    """Lista todos los estados de producto"""
    return estado_producto_repository.listar()

def obtener_por_id(id: int):
    """Obtiene un estado por ID"""
    return estado_producto_repository.obtener_por_id(id)

def obtener_por_nombre(nombre: str):
    """Obtiene un estado por nombre"""
    return estado_producto_repository.obtener_por_nombre(nombre)

def crear(estado: EstadoProducto):
    """Crea un nuevo estado"""
    return estado_producto_repository.crear(estado)

def actualizar(estado: EstadoProducto):
    """Actualiza un estado"""
    return estado_producto_repository.actualizar(estado)

def eliminar(id: int):
    """Elimina un estado"""
    estado_producto_repository.eliminar(id)

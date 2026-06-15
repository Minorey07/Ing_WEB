from repositorio import estado_pedido_repository
from esquema.estado_pedido import EstadoPedido

def listar():
    """Lista todos los estados de pedido"""
    return estado_pedido_repository.listar()

def obtener_por_id(id: int):
    """Obtiene un estado por ID"""
    return estado_pedido_repository.obtener_por_id(id)

def obtener_por_nombre(nombre: str):
    """Obtiene un estado por nombre"""
    return estado_pedido_repository.obtener_por_nombre(nombre)

def crear(estado: EstadoPedido):
    """Crea un nuevo estado"""
    return estado_pedido_repository.crear(estado)

def actualizar(estado: EstadoPedido):
    """Actualiza un estado"""
    return estado_pedido_repository.actualizar(estado)

def eliminar(id: int):
    """Elimina un estado"""
    estado_pedido_repository.eliminar(id)

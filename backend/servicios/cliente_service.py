from repositorio import cliente_repository, ubicacion_local_repository
from repositorio.serializador import serializar_cliente

def listar():
    """Lista clientes con relaciones serializadas"""
    clientes = cliente_repository.listar()
    ubicaciones = ubicacion_local_repository.listar()
    return [serializar_cliente(c, ubicaciones) for c in clientes]

def obtener_por_id(id: int):
    """Obtiene un cliente con relaciones serializadas"""
    cliente = cliente_repository.obtener_por_id(id) if hasattr(cliente_repository, 'obtener_por_id') else None
    if not cliente:
        clientes = cliente_repository.listar()
        cliente = next((c for c in clientes if c.id == id), None)
    
    if cliente:
        ubicaciones = ubicacion_local_repository.listar()
        return serializar_cliente(cliente, ubicaciones)
    return None

def crear(c):
    """Crea un cliente y lo retorna serializado"""
    cliente = cliente_repository.crear(c)
    ubicaciones = ubicacion_local_repository.listar()
    return serializar_cliente(cliente, ubicaciones)

def actualizar(c):
    """Actualiza un cliente y lo retorna serializado"""
    cliente = cliente_repository.actualizar(c)
    if cliente:
        ubicaciones = ubicacion_local_repository.listar()
        return serializar_cliente(cliente, ubicaciones)
    return None

def eliminar(id):
    """Elimina un cliente"""
    return cliente_repository.eliminar(id)
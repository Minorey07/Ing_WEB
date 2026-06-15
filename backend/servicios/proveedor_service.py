from repositorio import proveedor_repository, ubicacion_nacional_repository
from repositorio.serializador import serializar_proveedor

def listar():
    """Lista proveedores con relaciones serializadas"""
    proveedores = proveedor_repository.listar()
    ubicaciones = ubicacion_nacional_repository.listar()
    return [serializar_proveedor(p, ubicaciones) for p in proveedores]

def obtener_por_id(id: int):
    """Obtiene un proveedor con relaciones serializadas"""
    proveedor = proveedor_repository.obtener_por_id(id) if hasattr(proveedor_repository, 'obtener_por_id') else None
    if not proveedor:
        proveedores = proveedor_repository.listar()
        proveedor = next((p for p in proveedores if p.id == id), None)
    
    if proveedor:
        ubicaciones = ubicacion_nacional_repository.listar()
        return serializar_proveedor(proveedor, ubicaciones)
    return None

def crear(proveedor):
    """Crea un proveedor y lo retorna serializado"""
    nuevo_proveedor = proveedor_repository.crear(proveedor)
    ubicaciones = ubicacion_nacional_repository.listar()
    return serializar_proveedor(nuevo_proveedor, ubicaciones)

def actualizar(proveedor):
    """Actualiza un proveedor y lo retorna serializado"""
    proveedor_actualizado = proveedor_repository.actualizar(proveedor)
    if proveedor_actualizado:
        ubicaciones = ubicacion_nacional_repository.listar()
        return serializar_proveedor(proveedor_actualizado, ubicaciones)
    return None

def eliminar(id):
    """Elimina un proveedor"""
    return proveedor_repository.eliminar(id)

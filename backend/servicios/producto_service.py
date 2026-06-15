from repositorio import producto_repository, categoria_repository, estado_producto_repository
from repositorio.serializador import serializar_producto

def listar():
    """Lista productos con relaciones serializadas"""
    productos = producto_repository.listar()
    categorias = categoria_repository.listar()
    estados = estado_producto_repository.listar()
    return [serializar_producto(p, categorias, estados) for p in productos]

def obtener_por_id(id: int):
    """Obtiene un producto con relaciones serializadas"""
    producto = producto_repository.obtener_por_id(id) if hasattr(producto_repository, 'obtener_por_id') else None
    if not producto:
        productos = producto_repository.listar()
        producto = next((p for p in productos if p.id == id), None)
    
    if producto:
        categorias = categoria_repository.listar()
        estados = estado_producto_repository.listar()
        return serializar_producto(producto, categorias, estados)
    return None

def crear(p):
    """Crea un producto y lo retorna serializado"""
    producto = producto_repository.crear(p)
    categorias = categoria_repository.listar()
    estados = estado_producto_repository.listar()
    return serializar_producto(producto, categorias, estados)

def actualizar(p):
    """Actualiza un producto y lo retorna serializado"""
    producto = producto_repository.actualizar(p)
    if producto:
        categorias = categoria_repository.listar()
        estados = estado_producto_repository.listar()
        return serializar_producto(producto, categorias, estados)
    return None

def eliminar(id):
    """Elimina un producto"""
    return producto_repository.eliminar(id)

# 🔥 NUEVO: descontar stock
def descontar_stock(pedido):
    """Descuenta stock de productos en un pedido"""
    for d in pedido.detalles:
        productos = producto_repository.listar()
        producto = next((p for p in productos if p.id == d.producto_id), None)
        if producto:
            if producto.stock < d.cantidad:
                raise Exception(f"Sin stock suficiente para producto {d.producto_id}")
            producto.stock -= d.cantidad
            producto_repository.actualizar(producto)
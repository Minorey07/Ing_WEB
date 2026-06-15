from repositorio import pedido_repository, estado_pedido_repository
from repositorio.serializador import serializar_pedido, serializar_pedido_detalle
from servicios import producto_service

def listar():
    """Lista pedidos con relaciones serializadas"""
    pedidos = pedido_repository.listar()
    estados = estado_pedido_repository.listar()
    return [serializar_pedido(p, estados) for p in pedidos]

def obtener_por_id(id: int):
    """Obtiene un pedido con relaciones serializadas"""
    pedido = pedido_repository.obtener_por_id(id) if hasattr(pedido_repository, 'obtener_por_id') else None
    if not pedido:
        pedidos = pedido_repository.listar()
        pedido = next((p for p in pedidos if p.id == id), None)
    
    if pedido:
        estados = estado_pedido_repository.listar()
        detalles = [serializar_pedido_detalle(d) for d in pedido.detalles]
        return serializar_pedido(pedido, estados, detalles)
    return None

def crear(pedido):
    """Crea un pedido validando stock y lo retorna serializado"""
    # 🔥 validar stock antes de guardar
    for det in pedido.detalles:
        productos = producto_service.listar()
        producto = next((p for p in productos if p.id == det.producto_id), None)
        if producto and producto.get('stock', 0) < det.cantidad:
            raise Exception(f"Sin stock suficiente para producto {det.producto_id}")
    
    # Descontar stock
    producto_service.descontar_stock(pedido)
    
    nuevo_pedido = pedido_repository.crear(pedido)
    estados = estado_pedido_repository.listar()
    detalles = [serializar_pedido_detalle(d) for d in nuevo_pedido.detalles]
    return serializar_pedido(nuevo_pedido, estados, detalles)

def actualizar(pedido):
    """Actualiza un pedido y lo retorna serializado"""
    pedido_actualizado = pedido_repository.actualizar(pedido)
    if pedido_actualizado:
        estados = estado_pedido_repository.listar()
        detalles = [serializar_pedido_detalle(d) for d in pedido_actualizado.detalles]
        return serializar_pedido(pedido_actualizado, estados, detalles)
    return None

def eliminar(id):
    """Elimina un pedido"""
    return pedido_repository.eliminar(id)
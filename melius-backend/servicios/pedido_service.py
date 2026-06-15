from repositorio import pedido_repository
from servicios import producto_service

def listar():
    return pedido_repository.listar()

def crear(pedido):

    # 🔥 validar stock antes de guardar
    for det in pedido.detalles:
        producto_service.descontar_stock(
            det.producto_id,
            det.cantidad
        )

    return pedido_repository.crear(pedido)

def actualizar(pedido):
    return pedido_repository.actualizar(pedido)

def eliminar(id):
    return pedido_repository.eliminar(id)
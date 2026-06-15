from repositorio import pedido_repository
from servicios import producto_service

def listar():
    return pedido_repository.listar()

def crear(pedido):
    for det in pedido.detalles:
        producto_service.descontar_stock(det.producto_id, det.cantidad)
    data = pedido.model_dump(exclude={"id"})
    data["detalles"] = [d.model_dump() for d in pedido.detalles]
    return pedido_repository.crear(data)

def actualizar(pedido):
    data = pedido.model_dump()
    data["detalles"] = [d.model_dump() for d in pedido.detalles]
    return pedido_repository.actualizar(data)

def eliminar(id):
    return pedido_repository.eliminar(id)

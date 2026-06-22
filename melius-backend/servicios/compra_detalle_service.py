from repositorio import compra_detalle_repository
from servicios import producto_service

def listar():
    return compra_detalle_repository.listar()

def crear(data: dict):
    data.pop("producto_nombre", None)
    detalle = compra_detalle_repository.crear(data)
    if detalle:
        producto_service.incrementar_stock(data["producto_id"], data["cantidad"])
    return detalle

def actualizar(c):
    return compra_detalle_repository.actualizar(c)

def eliminar(id: int):
    return compra_detalle_repository.eliminar(id)
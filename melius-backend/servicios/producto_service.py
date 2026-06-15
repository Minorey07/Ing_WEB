from repositorio import producto_repository

def listar():
    return producto_repository.listar()

def crear(p):
    return producto_repository.crear(p)

def actualizar(p):
    return producto_repository.actualizar(p)

def eliminar(id):
    return producto_repository.eliminar(id)

# 🔥 NUEVO: descontar stock
def descontar_stock(pedido):
    for d in pedido.detalles:
        producto = buscar_producto(d.producto_id)
        if producto.stock < d.cantidad:
            raise Exception("Sin stock")
        producto.stock -= d.cantidad
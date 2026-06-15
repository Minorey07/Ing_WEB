from repositorio import pedido_repository, producto_repository

def resumen():
    pedidos = pedido_repository.listar()
    productos = producto_repository.listar()

    total_ventas = sum(p.total for p in pedidos)
    pendientes = len([p for p in pedidos if p.estado == "PENDIENTE"])
    entregados = len([p for p in pedidos if p.estado == "ENTREGADO"])

    stock_total = sum(p.stock for p in productos)

    return {
        "total_ventas": total_ventas,
        "pendientes": pendientes,
        "entregados": entregados,
        "productos_stock": stock_total
    }
from repositorio import pedido_repository, producto_repository

def resumen():
    pedidos = pedido_repository.listar()
    productos = producto_repository.listar()

    total_ventas = sum(p.get("total", 0) for p in pedidos)
    pendientes = len([p for p in pedidos if p.get("estado_id") == 1])
    entregados = len([p for p in pedidos if p.get("estado_id") == 2])
    stock_total = sum(p.get("stock", 0) for p in productos)

    return {
        "total_ventas": total_ventas,
        "pendientes": pendientes,
        "entregados": entregados,
        "productos_stock": stock_total,
    }

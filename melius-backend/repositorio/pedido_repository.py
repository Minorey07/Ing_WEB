from esquema.pedido import Pedido

pedidos = []

def listar():
    return pedidos

def crear(p: Pedido):
    p.id = len(pedidos) + 1
    pedidos.append(p)
    return p

def actualizar(p: Pedido):
    for i, item in enumerate(pedidos):
        if item.id == p.id:
            pedidos[i] = p
            return p

def eliminar(id: int):
    global pedidos
    pedidos = [p for p in pedidos if p.id != id]
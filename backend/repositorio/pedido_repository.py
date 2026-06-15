from esquema.pedido import Pedido

pedidos = []

def listar():
    return pedidos

def crear(p: Pedido):
    p.id = len(pedidos) + 1
    # Establecer estado_id por defecto a 1 (PENDIENTE)
    if not hasattr(p, 'estado_id') or p.estado_id is None:
        p.estado_id = 1
    pedidos.append(p)
    return p

def obtener_por_id(id: int):
    return next((p for p in pedidos if p.id == id), None)

def actualizar(p: Pedido):
    for i, item in enumerate(pedidos):
        if item.id == p.id:
            pedidos[i] = p
            return p
    return None

def eliminar(id: int):
    global pedidos
    pedidos = [p for p in pedidos if p.id != id]
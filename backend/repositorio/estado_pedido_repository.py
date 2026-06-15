from esquema.estado_pedido import EstadoPedido

# Base de datos en memoria - Estados de Pedido
estados_pedido = [
    EstadoPedido(id=1, nombre="PENDIENTE", descripcion="Pedido pendiente de procesar", es_final=False),
    EstadoPedido(id=2, nombre="CONFIRMADO", descripcion="Pedido confirmado", es_final=False),
    EstadoPedido(id=3, nombre="EN_TRANSITO", descripcion="Pedido en camino", es_final=False),
    EstadoPedido(id=4, nombre="ENTREGADO", descripcion="Pedido entregado", es_final=True),
    EstadoPedido(id=5, nombre="CANCELADO", descripcion="Pedido cancelado", es_final=True),
    EstadoPedido(id=6, nombre="DEVUELTO", descripcion="Pedido devuelto", es_final=True),
]

def listar():
    """Retorna todos los estados de pedido"""
    return estados_pedido

def obtener_por_id(id: int):
    """Obtiene un estado por ID"""
    for e in estados_pedido:
        if e.id == id:
            return e
    return None

def obtener_por_nombre(nombre: str):
    """Obtiene un estado por nombre"""
    for e in estados_pedido:
        if e.nombre.upper() == nombre.upper():
            return e
    return None

def crear(estado: EstadoPedido):
    """Crea un nuevo estado"""
    nueva_id = max([e.id for e in estados_pedido], default=0) + 1
    estado.id = nueva_id
    estados_pedido.append(estado)
    return estado

def actualizar(estado: EstadoPedido):
    """Actualiza un estado existente"""
    for i, e in enumerate(estados_pedido):
        if e.id == estado.id:
            estados_pedido[i] = estado
            return estado
    return None

def eliminar(id: int):
    """Elimina un estado por ID"""
    global estados_pedido
    estados_pedido = [e for e in estados_pedido if e.id != id]

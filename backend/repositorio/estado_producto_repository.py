from esquema.estado_producto import EstadoProducto

# Base de datos en memoria - Estados de Producto
estados_producto = [
    EstadoProducto(id=1, nombre="ACTIVO", descripcion="Producto disponible para venta", es_disponible=True),
    EstadoProducto(id=2, nombre="AGOTADO", descripcion="Producto sin stock", es_disponible=False),
    EstadoProducto(id=3, nombre="DESCONTINUADO", descripcion="Producto descontinuado", es_disponible=False),
    EstadoProducto(id=4, nombre="EN_MANTENIMIENTO", descripcion="Producto en mantenimiento temporal", es_disponible=False),
    EstadoProducto(id=5, nombre="DAÑADO", descripcion="Producto dañado o defectuoso", es_disponible=False),
]

def listar():
    """Retorna todos los estados de producto"""
    return estados_producto

def obtener_por_id(id: int):
    """Obtiene un estado por ID"""
    for e in estados_producto:
        if e.id == id:
            return e
    return None

def obtener_por_nombre(nombre: str):
    """Obtiene un estado por nombre"""
    for e in estados_producto:
        if e.nombre.upper() == nombre.upper():
            return e
    return None

def crear(estado: EstadoProducto):
    """Crea un nuevo estado"""
    nueva_id = max([e.id for e in estados_producto], default=0) + 1
    estado.id = nueva_id
    estados_producto.append(estado)
    return estado

def actualizar(estado: EstadoProducto):
    """Actualiza un estado existente"""
    for i, e in enumerate(estados_producto):
        if e.id == estado.id:
            estados_producto[i] = estado
            return estado
    return None

def eliminar(id: int):
    """Elimina un estado por ID"""
    global estados_producto
    estados_producto = [e for e in estados_producto if e.id != id]

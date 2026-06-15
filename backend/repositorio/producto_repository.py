productos = []

def listar():
    return productos

def crear(p):
    p.id = len(productos) + 1
    # Establecer estado_id por defecto a 1 (ACTIVO)
    if not hasattr(p, 'estado_id') or p.estado_id is None:
        p.estado_id = 1
    productos.append(p)
    return p

def obtener_por_id(id: int):
    return next((p for p in productos if p.id == id), None)

def actualizar(p):
    for i, item in enumerate(productos):
        if item.id == p.id:
            productos[i] = p
            return p
    return None

def eliminar(id):
    global productos
    productos = [p for p in productos if p.id != id]
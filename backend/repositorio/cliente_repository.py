clientes = []

def listar():
    return clientes

def crear(c):
    c.id = len(clientes) + 1
    # Establecer ubicacion_local_id por defecto a 1 (Huancayo)
    if not hasattr(c, 'ubicacion_local_id') or c.ubicacion_local_id is None:
        c.ubicacion_local_id = 1
    clientes.append(c)
    return c

def obtener_por_id(id: int):
    return next((c for c in clientes if c.id == id), None)

def actualizar(c):
    for i, item in enumerate(clientes):
        if item.id == c.id:
            clientes[i] = c
            return c
    return None

def eliminar(id):
    global clientes
    clientes = [c for c in clientes if c.id != id]
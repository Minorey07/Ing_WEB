usuarios = []

def listar():
    return usuarios

def crear(u):
    u.id = len(usuarios) + 1
    # Establecer rol_id por defecto a 3 (VENDEDOR)
    if not hasattr(u, 'rol_id') or u.rol_id is None:
        u.rol_id = 3
    usuarios.append(u)
    return u

def obtener_por_id(id: int):
    return next((u for u in usuarios if u.id == id), None)

def actualizar(u):
    for i, item in enumerate(usuarios):
        if item.id == u.id:
            usuarios[i] = u
            return u
    return None

def eliminar(id):
    global usuarios
    usuarios = [u for u in usuarios if u.id != id]
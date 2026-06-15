usuarios = []

def listar():
    return usuarios

def crear(c):
    c.id = len(usuarios) + 1
    usuarios.append(c)
    return c

def actualizar(c):
    for i, item in enumerate(usuarios):
        if item.id == c.id:
            usuarios[i] = c
            return c

def eliminar(id):
    global usuarios
    usuarios = [c for c in usuarios if c.id != id]
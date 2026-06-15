clientes = []

def listar():
    return clientes

def crear(c):
    c.id = len(clientes) + 1
    clientes.append(c)
    return c

def actualizar(c):
    for i, item in enumerate(clientes):
        if item.id == c.id:
            clientes[i] = c
            return c

def eliminar(id):
    global clientes
    clientes = [c for c in clientes if c.id != id]
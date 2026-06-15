productos = []

def listar():
    return productos

def crear(p):
    p.id = len(productos) + 1
    productos.append(p)
    return p

def actualizar(p):
    for i, item in enumerate(productos):
        if item.id == p.id:
            productos[i] = p
            return p

def eliminar(id):
    global productos
    productos = [p for p in productos if p.id != id]
from repositorio import proveedor_repository

def listar():
    return proveedor_repository.listar()

def crear(p):
    return proveedor_repository.crear(p)

def actualizar(p):
    return proveedor_repository.actualizar(p)

def eliminar(id):
    return proveedor_repository.eliminar(id)

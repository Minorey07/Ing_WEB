from repositorio import compra_repository

def listar():
    return compra_repository.listar()

def crear(c):
    return compra_repository.crear(c)

def actualizar(c):
    return compra_repository.actualizar(c)

def eliminar(id):
    return compra_repository.eliminar(id)

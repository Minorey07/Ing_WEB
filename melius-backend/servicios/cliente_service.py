from repositorio import cliente_repository

def listar():
    return cliente_repository.listar()

def crear(c):
    return cliente_repository.crear(c)

def actualizar(c):
    return cliente_repository.actualizar(c)

def eliminar(id):
    return cliente_repository.eliminar(id)
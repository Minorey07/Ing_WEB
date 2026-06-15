from repositorio import usuario_repository

def listar():
    return usuario_repository.listar()

def crear(c):
    return usuario_repository.crear(c)

def actualizar(c):
    return usuario_repository.actualizar(c)

def eliminar(id):
    return usuario_repository.eliminar(id)
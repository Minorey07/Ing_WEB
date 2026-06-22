from repositorio import usuario_repository

def listar():
    return usuario_repository.listar()

def crear(u):
    return usuario_repository.crear(u)

def actualizar(u):
    return usuario_repository.actualizar(u)

def eliminar(id):
    return usuario_repository.eliminar(id)

def verificar_login(correo: str, password: str):
    usuarios = usuario_repository.listar()
    for u in usuarios:
        if u.get("correo") == correo and u.get("password") == password:
            return u
    return None

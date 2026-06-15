from repositorio import usuario_repository, rol_repository
from repositorio.serializador import serializar_usuario

def listar():
    """Lista usuarios con relaciones serializadas"""
    usuarios = usuario_repository.listar()
    roles = rol_repository.listar()
    return [serializar_usuario(u, roles) for u in usuarios]

def obtener_por_id(id: str):
    """Obtiene un usuario con relaciones serializadas"""
    usuario = usuario_repository.obtener_por_id(id) if hasattr(usuario_repository, 'obtener_por_id') else None
    if not usuario:
        usuarios = usuario_repository.listar()
        usuario = next((u for u in usuarios if u.id == id), None)
    
    if usuario:
        roles = rol_repository.listar()
        return serializar_usuario(usuario, roles)
    return None

def crear(c):
    """Crea un usuario y lo retorna serializado"""
    usuario = usuario_repository.crear(c)
    roles = rol_repository.listar()
    return serializar_usuario(usuario, roles)

def actualizar(c):
    """Actualiza un usuario y lo retorna serializado"""
    usuario = usuario_repository.actualizar(c)
    if usuario:
        roles = rol_repository.listar()
        return serializar_usuario(usuario, roles)
    return None

def eliminar(id):
    """Elimina un usuario"""
    return usuario_repository.eliminar(id)
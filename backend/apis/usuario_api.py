from fastapi import APIRouter, HTTPException
from esquema.usuario import Usuario
from servicios import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/")
def listar_usuarios():
    """Obtiene todos los usuarios"""
    return usuario_service.listar()

@router.get("/{id}")
def obtener_usuario(id: int):
    """Obtiene un usuario por ID"""
    usuario = usuario_service.obtener_por_id(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/")
def crear_usuario(u: Usuario):
    """Crea un nuevo usuario"""
    return usuario_service.crear(u)

@router.put("/{id}")
def actualizar_usuario(id: int, u: Usuario):
    """Actualiza un usuario"""
    u.id = id
    resultado = usuario_service.actualizar(u)
    if not resultado:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar_usuario(id: int):
    """Elimina un usuario"""
    usuario = usuario_service.obtener_por_id(id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_service.eliminar(id)
    return {"mensaje": "Usuario eliminado exitosamente"}

@router.post("/login")
def login(user: Usuario):
    """Login de usuario por nombre y contraseña"""
    usuarios = usuario_service.listar()
    for u in usuarios:
        if u.get('nombre') == user.nombre and u.get('password') == user.password:
            return {"ok": True, "usuario": u}
    return {"ok": False}
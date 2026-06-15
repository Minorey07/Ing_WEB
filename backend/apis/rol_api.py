from fastapi import APIRouter, HTTPException
from esquema.rol import Rol
from servicios import rol_service

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def obtener_todos_roles():
    """Obtiene todos los roles"""
    return rol_service.listar()

@router.get("/{id}")
def obtener_rol(id: int):
    """Obtiene un rol por ID"""
    rol = rol_service.obtener_por_id(id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return rol

@router.post("/")
def crear_rol(rol: Rol):
    """Crea un nuevo rol"""
    return rol_service.crear(rol)

@router.put("/{id}")
def actualizar_rol(id: int, rol: Rol):
    """Actualiza un rol"""
    rol.id = id
    resultado = rol_service.actualizar(rol)
    if not resultado:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return resultado

@router.delete("/{id}")
def eliminar_rol(id: int):
    """Elimina un rol"""
    rol = rol_service.obtener_por_id(id)
    if not rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    rol_service.eliminar(id)
    return {"mensaje": "Rol eliminado exitosamente"}


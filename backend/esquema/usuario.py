from pydantic import BaseModel
from typing import Optional

class Rol(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    permisos: str | None = None

class Usuario(BaseModel):
    id: int | None = None
    nombre: str
    correo: str
    password: str
    rol_id: int
    rol: Optional[Rol] = None  # Para serialización
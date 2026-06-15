from pydantic import BaseModel

class Rol(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    permisos: str | None = None

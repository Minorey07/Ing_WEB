from pydantic import BaseModel

class Usuario(BaseModel):
    id: int | None = None
    nombre: str
    correo: str = ""
    rol_id: int
    rol_nombre: str | None = None
    password: str
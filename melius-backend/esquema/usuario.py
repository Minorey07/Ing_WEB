from pydantic import BaseModel

class Usuario(BaseModel):
    id: int | None = None
    nombre: str
    rol: str
    password: str
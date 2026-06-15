from pydantic import BaseModel

class Categoria(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None

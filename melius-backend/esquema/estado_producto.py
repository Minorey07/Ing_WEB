from pydantic import BaseModel

class EstadoProducto(BaseModel):
    id: int | None = None
    nombre: str

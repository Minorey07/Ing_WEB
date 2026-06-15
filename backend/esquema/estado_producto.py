from pydantic import BaseModel

class EstadoProducto(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    es_disponible: bool = True

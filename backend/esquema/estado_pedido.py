from pydantic import BaseModel

class EstadoPedido(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    es_final: bool = False

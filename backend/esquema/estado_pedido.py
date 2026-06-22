from pydantic import BaseModel

class EstadoPedido(BaseModel):
    id: int | None = None
    nombre: str

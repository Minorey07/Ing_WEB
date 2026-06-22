from pydantic import BaseModel
from typing import List

class PedidoDetalle(BaseModel):
    producto_id: int
    cantidad: int
    precio: float
    subtotal: float

class Pedido(BaseModel):
    id: int | None = None
    cliente_id: int
    vendedor_id: int
    estado_id: int = 1
    estado_nombre: str | None = None
    total: float
    detalles: List[PedidoDetalle]
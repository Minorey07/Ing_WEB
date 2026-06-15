from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EstadoPedido(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    es_final: bool = False

class PedidoDetalle(BaseModel):
    id: int | None = None
    producto_id: int
    cantidad: int
    precio: float
    subtotal: float

class Pedido(BaseModel):
    id: int | None = None
    cliente_id: int
    vendedor_id: int
    fecha: datetime
    estado_id: int
    total: float
    detalles: List[PedidoDetalle]
    estado: Optional[EstadoPedido] = None  # Para serialización
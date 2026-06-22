from pydantic import BaseModel
from datetime import datetime
from typing import List

class CompraDetalleOut(BaseModel):
    id: int | None = None
    compra_id: int | None = None
    producto_id: int
    producto_nombre: str | None = None
    cantidad: int
    precio: float
    subtotal: float

class Compra(BaseModel):
    id: int | None = None
    proveedor_id: int
    proveedor_nombre: str | None = None
    total: float
    detalles: List[CompraDetalleOut] | None = None
    created_at: datetime | None = None

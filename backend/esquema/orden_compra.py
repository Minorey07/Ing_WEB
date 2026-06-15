from pydantic import BaseModel
from datetime import datetime

class OrdenCompra(BaseModel):
    id: int | None = None
    proveedor_id: int
    comprador_id: int
    fecha_pedido: datetime
    fecha_recepcion: datetime | None = None
    total_compra: float = 0.0
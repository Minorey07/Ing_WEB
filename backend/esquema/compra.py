from pydantic import BaseModel
from datetime import datetime

class Compra(BaseModel):
    id: int | None = None
    proveedor_id: int
    fecha: datetime
    total: float

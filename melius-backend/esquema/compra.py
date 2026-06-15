from pydantic import BaseModel
from datetime import datetime

class Compra(BaseModel):
    id: int | None = None
    proveedor_id: int
    total: float
    created_at: datetime | None = None

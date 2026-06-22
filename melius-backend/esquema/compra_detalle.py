from pydantic import BaseModel

class CompraDetalle(BaseModel):
    id: int | None = None
    compra_id: int
    producto_id: int
    producto_nombre: str | None = None
    cantidad: int
    precio: float
    subtotal: float
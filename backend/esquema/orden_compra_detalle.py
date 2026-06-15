from pydantic import BaseModel

class OrdenCompraDetalle(BaseModel):
    id: int | None = None
    orden_compra_id: int
    producto_id: int
    cantidad_solicitada: int
    cantidad_recibida: int = 0
    precio_compra_unitario: float
    subtotal: float
from pydantic import BaseModel

class ProveedorProducto(BaseModel):
    id: int | None = None
    proveedor_id: int
    producto_id: int
    precio_sugerido: float

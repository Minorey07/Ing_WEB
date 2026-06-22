from pydantic import BaseModel

class Producto(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str
    precio: float
    stock: int
    estado_id: int = 1
    estado_nombre: str | None = None
    categoria_id: int | None = None
    categoria_nombre: str | None = None
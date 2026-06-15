from pydantic import BaseModel
from typing import Optional

class Categoria(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None

class EstadoProducto(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    es_disponible: bool = True

class Producto(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str
    precio: float
    stock: int
    presentacion: str | None = None
    categoria_id: int
    estado_id: int
    categoria: Optional[Categoria] = None  # Para serialización
    estado: Optional[EstadoProducto] = None  # Para serialización
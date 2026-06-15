from pydantic import BaseModel
from typing import Optional

class UbicacionNacional(BaseModel):
    id: int | None = None
    direccion: str
    telefono: str
    ciudad: str
    departamento: str
    pais: str = "Perú"

class Proveedor(BaseModel):
    id: int | None = None
    razon_social: str
    ruc: str
    ubicacion_nacional_id: int
    ubicacion: Optional[UbicacionNacional] = None  # Para serialización

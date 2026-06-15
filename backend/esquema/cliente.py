from pydantic import BaseModel
from typing import Optional

class UbicacionLocal(BaseModel):
    id: int | None = None
    direccion: str
    telefono: str
    distrito: str

class Cliente(BaseModel):
    id: int | None = None
    nombres: str
    ubicacion_local_id: int
    ubicacion: Optional[UbicacionLocal] = None  # Para serialización
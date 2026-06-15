from pydantic import BaseModel

class UbicacionLocal(BaseModel):
    id: int | None = None
    direccion: str
    telefono: str
    distrito: str

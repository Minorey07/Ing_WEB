from pydantic import BaseModel

class UbicacionNacional(BaseModel):
    id: int | None = None
    direccion: str
    telefono: str
    ciudad: str
    departamento: str
    pais: str = "Perú"

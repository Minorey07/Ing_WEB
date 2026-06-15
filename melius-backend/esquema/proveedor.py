from pydantic import BaseModel

class Proveedor(BaseModel):
    id: int | None = None
    razon_social: str
    ruc: str
    telefono: str = ""
    direccion: str = ""

from pydantic import BaseModel

class Cliente(BaseModel):
    id: int | None = None
    nombres: str
    telefono: str
    direccion: str
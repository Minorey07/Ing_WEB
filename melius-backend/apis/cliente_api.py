from fastapi import APIRouter
from esquema.cliente import Cliente

router = APIRouter(prefix="/clientes", tags=["Clientes"])

clientes = []

@router.get("/")
def listar():
    return clientes

@router.post("/")
def crear(c: Cliente):
    c.id = len(clientes) + 1
    clientes.append(c)
    return c
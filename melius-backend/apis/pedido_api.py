from fastapi import APIRouter
from esquema.pedido import Pedido

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

pedidos = []

@router.get("/")
def listar():
    return pedidos

@router.post("/")
def crear(p: Pedido):
    p.id = len(pedidos) + 1
    pedidos.append(p)
    return p
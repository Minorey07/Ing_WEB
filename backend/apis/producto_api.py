from fastapi import APIRouter
from esquema.producto import Producto
from servicios import producto_service

router = APIRouter(prefix="/productos", tags=["Productos"])

@router.get("/")
def listar():
    return producto_service.listar()

@router.post("/")
def crear(p: Producto):
    return producto_service.crear(p)

@router.put("/")
def actualizar(p: Producto):
    return producto_service.actualizar(p)

@router.delete("/{id}")
def eliminar(id: int):
    return producto_service.eliminar(id)
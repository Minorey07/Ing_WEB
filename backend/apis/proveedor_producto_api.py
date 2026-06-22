from fastapi import APIRouter, Depends

from esquema.proveedor_producto import ProveedorProducto
from auth.dependencies import get_current_user, require_roles
from repositorio import proveedor_producto_repository

router = APIRouter(prefix="/proveedor-productos", tags=["ProveedorProductos"])


@router.get("/")
def listar(current_user: dict = Depends(get_current_user)):
    data = proveedor_producto_repository.listar()
    return {"ok": True, "data": data}


@router.post("/")
def crear(p: ProveedorProducto, current_user: dict = Depends(require_roles(["ADMIN", "ALMACENERO"]))):
    data = proveedor_producto_repository.crear(p)
    return {"ok": True, "data": data}


@router.put("/{id}")
def actualizar(id: int, p: ProveedorProducto, current_user: dict = Depends(require_roles(["ADMIN", "ALMACENERO"]))):
    p.id = id
    data = proveedor_producto_repository.actualizar(p)
    return {"ok": True, "data": data}


@router.delete("/{id}")
def eliminar(id: int, current_user: dict = Depends(require_roles(["ADMIN"]))):
    proveedor_producto_repository.eliminar(id)
    return {"ok": True, "data": None}

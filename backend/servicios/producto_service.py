from repositorio import producto_repository

def listar():
    return producto_repository.listar()

def crear(p, rol_id: int = None):
    if rol_id is not None and rol_id == 3:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"ok": False, "error": "VENDEDOR no puede crear productos"},
        )
    return producto_repository.crear(p)

def actualizar(p, rol_id: int = None):
    if rol_id is not None and rol_id == 3:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"ok": False, "error": "VENDEDOR no puede modificar productos"},
        )
    return producto_repository.actualizar(p)

def eliminar(id):
    return producto_repository.eliminar(id)

def incrementar_stock(producto_id: int, cantidad: int):
    productos = producto_repository.listar()
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if not producto:
        from fastapi import HTTPException, status
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"ok": False, "error": "Producto no encontrado"})
    nuevo_stock = producto["stock"] + cantidad
    from esquema.producto import Producto
    prod = Producto(**producto)
    prod.stock = nuevo_stock
    producto_repository.actualizar(prod)

def descontar_stock(producto_id: int, cantidad: int):
    productos = producto_repository.listar()
    producto = next((p for p in productos if p["id"] == producto_id), None)
    if not producto:
        raise ValueError("Producto no encontrado")
    if producto["stock"] < cantidad:
        raise ValueError(f"Stock insuficiente para producto {producto['nombre']}")
    nuevo_stock = producto["stock"] - cantidad
    from esquema.producto import Producto
    prod = Producto(**producto)
    prod.stock = nuevo_stock
    producto_repository.actualizar(prod)

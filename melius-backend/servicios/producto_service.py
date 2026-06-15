from repositorio import producto_repository

def listar():
    return producto_repository.listar()

def crear(p):
    return producto_repository.crear(p)

def actualizar(p):
    return producto_repository.actualizar(p)

def eliminar(id):
    return producto_repository.eliminar(id)

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

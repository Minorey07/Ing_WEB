from esquema.proveedor import Proveedor

# Base de datos en memoria - Proveedores con datos iniciales
proveedores = [
    Proveedor(id=1, razon_social="Distribuidora Peruana SAC", ruc="20123456789", ubicacion_nacional_id=1),
    Proveedor(id=2, razon_social="Importaciones Andinas EIRL", ruc="20987654321", ubicacion_nacional_id=2),
    Proveedor(id=3, razon_social="Comercializadora del Sur", ruc="20555666777", ubicacion_nacional_id=3),
    Proveedor(id=4, razon_social="Productos Frescos Nacionales", ruc="20444333222", ubicacion_nacional_id=4),
]

def listar():
    """Retorna todos los proveedores"""
    return proveedores

def obtener_por_id(id: int):
    """Obtiene un proveedor por ID"""
    for p in proveedores:
        if p.id == id:
            return p
    return None

def obtener_por_ruc(ruc: str):
    """Obtiene un proveedor por RUC"""
    for p in proveedores:
        if p.ruc == ruc:
            return p
    return None

def crear(proveedor: Proveedor):
    """Crea un nuevo proveedor"""
    nueva_id = max([p.id for p in proveedores], default=0) + 1
    proveedor.id = nueva_id
    proveedores.append(proveedor)
    return proveedor

def actualizar(proveedor: Proveedor):
    """Actualiza un proveedor existente"""
    for i, p in enumerate(proveedores):
        if p.id == proveedor.id:
            proveedores[i] = proveedor
            return proveedor
    return None

def eliminar(id: int):
    """Elimina un proveedor por ID"""
    global proveedores
    proveedores = [p for p in proveedores if p.id != id]

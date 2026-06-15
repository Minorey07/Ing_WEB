from esquema.rol import Rol

# Base de datos en memoria - Roles de Usuario
roles = [
    Rol(id=1, nombre="ADMIN", descripcion="Administrador del sistema", permisos="*"),
    Rol(id=2, nombre="ALMACENERO", descripcion="Responsable del almacén", permisos="crear_producto,actualizar_producto,ver_inventario,ver_pedidos"),
    Rol(id=3, nombre="VENDEDOR", descripcion="Vendedor de la empresa", permisos="crear_pedido,ver_productos,ver_clientes,actualizar_pedido"),
]

def listar():
    """Retorna todos los roles"""
    return roles

def obtener_por_id(id: int):
    """Obtiene un rol por ID"""
    for r in roles:
        if r.id == id:
            return r
    return None

def obtener_por_nombre(nombre: str):
    """Obtiene un rol por nombre"""
    for r in roles:
        if r.nombre.upper() == nombre.upper():
            return r
    return None

def crear(rol: Rol):
    """Crea un nuevo rol"""
    nueva_id = max([r.id for r in roles], default=0) + 1
    rol.id = nueva_id
    roles.append(rol)
    return rol

def actualizar(rol: Rol):
    """Actualiza un rol existente"""
    for i, r in enumerate(roles):
        if r.id == rol.id:
            roles[i] = rol
            return rol
    return None

def eliminar(id: int):
    """Elimina un rol por ID"""
    global roles
    roles = [r for r in roles if r.id != id]

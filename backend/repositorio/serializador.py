# Módulo auxiliar para serialización de relaciones (resolución de FKs)
# Este módulo contiene funciones helper para resolver Foreign Keys
# y devolver los datos con las relaciones resueltas al frontend

def serializar_producto(producto, categorias=None, estados_producto=None):
    """
    Serializa un producto resolviendo sus FK de categoria y estado
    
    Args:
        producto: Instancia de Producto
        categorias: Lista de categorías disponibles
        estados_producto: Lista de estados de producto disponibles
    
    Returns:
        Dict con producto serializado con objetos de categoria y estado
    """
    if not producto:
        return None
    
    resultado = {
        'id': producto.id,
        'nombre': producto.nombre,
        'descripcion': producto.descripcion,
        'precio': producto.precio,
        'stock': producto.stock,
        'presentacion': getattr(producto, 'presentacion', None),
        'categoria_id': getattr(producto, 'categoria_id', None),
        'estado_id': getattr(producto, 'estado_id', None),
    }
    
    # Resolver categoria si existe
    if categorias and hasattr(producto, 'categoria_id'):
        categoria = next((c for c in categorias if c.id == producto.categoria_id), None)
        if categoria:
            resultado['categoria'] = {
                'id': categoria.id,
                'nombre': categoria.nombre,
                'descripcion': getattr(categoria, 'descripcion', None)
            }
    
    # Resolver estado si existe
    if estados_producto and hasattr(producto, 'estado_id'):
        estado = next((e for e in estados_producto if e.id == producto.estado_id), None)
        if estado:
            resultado['estado'] = {
                'id': estado.id,
                'nombre': estado.nombre,
                'descripcion': getattr(estado, 'descripcion', None),
                'es_disponible': getattr(estado, 'es_disponible', True)
            }
    
    return resultado


def serializar_usuario(usuario, roles=None):
    """Serializa un usuario resolviendo su FK de rol"""
    if not usuario:
        return None
    
    resultado = {
        'id': usuario.id,
        'nombre': usuario.nombre,
        'correo': usuario.correo,
        'password': usuario.password,
        'rol_id': getattr(usuario, 'rol_id', None),
    }
    
    # Resolver rol si existe
    if roles and hasattr(usuario, 'rol_id'):
        rol = next((r for r in roles if r.id == usuario.rol_id), None)
        if rol:
            resultado['rol'] = {
                'id': rol.id,
                'nombre': rol.nombre,
                'descripcion': getattr(rol, 'descripcion', None),
                'permisos': getattr(rol, 'permisos', None)
            }
    
    return resultado


def serializar_cliente(cliente, ubicaciones_locales=None):
    """Serializa un cliente resolviendo su FK de ubicacion_local"""
    if not cliente:
        return None
    
    resultado = {
        'id': cliente.id,
        'nombres': cliente.nombres,
        'ubicacion_local_id': getattr(cliente, 'ubicacion_local_id', None),
    }
    
    # Resolver ubicacion si existe
    if ubicaciones_locales and hasattr(cliente, 'ubicacion_local_id'):
        ubicacion = next((u for u in ubicaciones_locales if u.id == cliente.ubicacion_local_id), None)
        if ubicacion:
            resultado['ubicacion'] = {
                'id': ubicacion.id,
                'direccion': ubicacion.direccion,
                'telefono': ubicacion.telefono,
                'distrito': ubicacion.distrito
            }
    
    return resultado


def serializar_proveedor(proveedor, ubicaciones_nacionales=None):
    """Serializa un proveedor resolviendo su FK de ubicacion_nacional"""
    if not proveedor:
        return None
    
    resultado = {
        'id': proveedor.id,
        'razon_social': proveedor.razon_social,
        'ruc': proveedor.ruc,
        'ubicacion_nacional_id': getattr(proveedor, 'ubicacion_nacional_id', None),
    }
    
    # Resolver ubicacion si existe
    if ubicaciones_nacionales and hasattr(proveedor, 'ubicacion_nacional_id'):
        ubicacion = next((u for u in ubicaciones_nacionales if u.id == proveedor.ubicacion_nacional_id), None)
        if ubicacion:
            resultado['ubicacion'] = {
                'id': ubicacion.id,
                'direccion': ubicacion.direccion,
                'telefono': ubicacion.telefono,
                'ciudad': ubicacion.ciudad,
                'departamento': ubicacion.departamento,
                'pais': getattr(ubicacion, 'pais', 'Perú')
            }
    
    return resultado


def serializar_pedido(pedido, estados_pedido=None, detalles_resueltos=None):
    """Serializa un pedido resolviendo su FK de estado"""
    if not pedido:
        return None
    
    resultado = {
        'id': pedido.id,
        'cliente_id': pedido.cliente_id,
        'vendedor_id': pedido.vendedor_id,
        'fecha': pedido.fecha.isoformat() if hasattr(pedido.fecha, 'isoformat') else str(pedido.fecha),
        'estado_id': getattr(pedido, 'estado_id', None),
        'total': pedido.total,
        'detalles': detalles_resueltos or pedido.detalles
    }
    
    # Resolver estado si existe
    if estados_pedido and hasattr(pedido, 'estado_id'):
        estado = next((e for e in estados_pedido if e.id == pedido.estado_id), None)
        if estado:
            resultado['estado'] = {
                'id': estado.id,
                'nombre': estado.nombre,
                'descripcion': getattr(estado, 'descripcion', None),
                'es_final': getattr(estado, 'es_final', False)
            }
    
    return resultado


def serializar_pedido_detalle(detalle):
    """Serializa un detalle de pedido"""
    if not detalle:
        return None
    
    return {
        'id': getattr(detalle, 'id', None),
        'producto_id': detalle.producto_id,
        'cantidad': detalle.cantidad,
        'precio': detalle.precio,
        'subtotal': detalle.subtotal
    }

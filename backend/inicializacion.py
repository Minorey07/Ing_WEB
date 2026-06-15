# Archivo de inicialización de datos
# Este archivo contiene funciones para inicializar los datos en memoria
# cuando se inicia la aplicación

def inicializar_datos():
    """
    Inicializa todos los datos de catálogos cuando se inicia la aplicación
    
    Los datos ya están pre-poblados en los repositorios:
    - categoria_repository: 16 categorías de productos
    - estado_producto_repository: 5 estados de producto
    - estado_pedido_repository: 6 estados de pedido
    - rol_repository: 3 roles de usuario
    - ubicacion_local_repository: 5 ubicaciones en Huancayo
    - ubicacion_nacional_repository: 5 ubicaciones nacionales
    - proveedor_repository: 4 proveedores iniciales
    """
    
    # Los repositorios ya tienen datos iniciales
    # Solo se llama esta función para confirmación de carga
    
    from repositorio import (
        categoria_repository,
        estado_producto_repository,
        estado_pedido_repository,
        rol_repository,
        ubicacion_local_repository,
        ubicacion_nacional_repository,
        proveedor_repository
    )
    
    datos_iniciales = {
        "categorias": len(categoria_repository.listar()),
        "estados_producto": len(estado_producto_repository.listar()),
        "estados_pedido": len(estado_pedido_repository.listar()),
        "roles": len(rol_repository.listar()),
        "ubicaciones_locales": len(ubicacion_local_repository.listar()),
        "ubicaciones_nacionales": len(ubicacion_nacional_repository.listar()),
        "proveedores": len(proveedor_repository.listar()),
    }
    
    print("✅ DATOS INICIALES CARGADOS:")
    print(f"  - Categorías: {datos_iniciales['categorias']}")
    print(f"  - Estados de Producto: {datos_iniciales['estados_producto']}")
    print(f"  - Estados de Pedido: {datos_iniciales['estados_pedido']}")
    print(f"  - Roles: {datos_iniciales['roles']}")
    print(f"  - Ubicaciones Locales: {datos_iniciales['ubicaciones_locales']}")
    print(f"  - Ubicaciones Nacionales: {datos_iniciales['ubicaciones_nacionales']}")
    print(f"  - Proveedores: {datos_iniciales['proveedores']}")
    
    return datos_iniciales


def obtener_estado_inicial():
    """Retorna información del estado inicial de la aplicación"""
    try:
        datos = inicializar_datos()
        return {
            "status": "success",
            "mensaje": "Sistema inicializado correctamente",
            "datos": datos
        }
    except Exception as e:
        return {
            "status": "error",
            "mensaje": f"Error al inicializar: {str(e)}"
        }

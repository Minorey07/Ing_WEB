# Tasks: Mejora Compras, Compra Detalles y Control de Estados en Pedidos

## 1. Repositorios — JOINs para nombres asociados

- [x] 1.1 Agregar JOIN con `proveedores!inner(razon_social)` en `compra_repository.listar()` para devolver `proveedor_nombre`
- [x] 1.2 Agregar JOIN con `productos!inner(nombre)` en `compra_detalle_repository.listar()` para devolver `producto_nombre`

## 2. Servicio — Auto-stock en compra_detalles

- [x] 2.1 Crear `compra_detalle_service.py` con función `crear()` que inserta el detalle e incrementa `productos.stock += cantidad`
- [x] 2.2 Exponer endpoint `POST /compra-detalles/` en `compra_detalle_api.py` usando el nuevo servicio

## 3. API Pedidos — Control de estados

- [x] 3.1 Agregar en `pedido_service.py` función `actualizar_solo_estado(id, estado_id, rol_id)` que valida rol (solo 1 o 2) y bloquea si `estado_id >= 2`
- [x] 3.2 Agregar endpoint `PUT /pedidos/{id}/estado` en `pedido_api.py` que llama a `actualizar_solo_estado`

## 4. Frontend — Modelos TypeScript

- [x] 4.1 Agregar campo `proveedorNombre?: string` en `models/compra.model.ts`
- [x] 4.2 Agregar campo `productoNombre?: string` en `models/compra-detalle.model.ts`

## 5. Frontend — Renderizado de nombres

- [x] 5.1 Actualizar `compra-component.html` para mostrar `proveedorNombre` en columna de tabla
- [x] 5.2 (no existe compra-detalle-component — componente no creado, se salta)
- [x] 5.3 Mostrar `estadoNombre` en tabla de pedidos — ya está implementado en `pedido-component.html:189`

## 6. Verificación

- [x] 6.1 Probar que `POST /compra-detalles/` incrementa stock del producto correspondiente
- [x] 6.2 Probar que `PUT /pedidos/{id}/estado` rechaza VENDEDOR con 403
- [x] 6.3 Probar que `PUT /pedidos/{id}/estado` rechaza edición si estado >= 2
- [x] 6.4 Verificar `ng build` sin errores de compilación

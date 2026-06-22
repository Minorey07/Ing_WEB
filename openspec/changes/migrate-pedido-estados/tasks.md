## 1. Base de datos - Migración de esquema

- [ ] 1.1 Crear script SQL con tablas maestras: `roles`, `estados_pedido`, `categorias`, `estados_producto`, `ubicaciones_locales`, `ubicaciones_nacionales`
- [ ] 1.2 Crear script SQL con tablas extendidas de compras: `ordenes_compra`, `orden_compra_detalles`, `proveedor_productos`
- [ ] 1.3 Migrar `pedidos.estado` (TEXT) a `pedidos.estado_id` (BIGINT FK → estados_pedido)
- [ ] 1.4 Insertar datos semilla: roles (ADMIN, ALMACENERO, VENDEDOR), estados_pedido (PENDIENTE, ENTREGADO)

## 2. Backend - Validación de permisos

- [ ] 2.1 Actualizar `esquema/pedido.py`: reemplazar `estado: str` por `estado_id: int`
- [ ] 2.2 Actualizar `pedido_service.py`: validar que `current_user["rol"] != "VENDEDOR"` en `actualizar()`, asignar `estado_id=1` en `crear()`
- [ ] 2.3 Actualizar `pedido_api.py`: pasar `current_user` a `pedido_service.actualizar()` y manejar HTTP 403
- [ ] 2.4 Actualizar `pedido_repository.py`: usar `estado_id` en lugar de `estado` en inserts/updates

## 3. Frontend - Ocultar control de estado al VENDEDOR

- [ ] 3.1 Actualizar `models/pedido.model.ts`: reemplazar `estado: string` por `estadoId: number`
- [ ] 3.2 Actualizar `pedido-component.html`: ocultar selector de estado cuando `rol === 'VENDEDOR'`
- [ ] 3.3 Actualizar `pedido-component.ts`: adaptar `modeloPedido` para usar `estadoId`, enviar `estado_id=1` en nuevos pedidos si es VENDEDOR

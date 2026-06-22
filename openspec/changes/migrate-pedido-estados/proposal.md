## Why

El sistema actual maneja el estado de pedidos como texto libre (`estado: str`) y no restringe quién puede modificar ese estado. El VENDEDOR puede cambiar el estado de un pedido, lo que no es correcto según las reglas de negocio: solo ADMIN y ALMACENERO deben poder modificar el flujo de estado. Además, se requiere migrar de 7 a 15 tablas para normalizar el esquema con tablas maestras (estados_pedido, categorias, roles, etc.).

## What Changes

- **Backend**: Agregar validación de permisos en `PUT /pedidos/{id}` — solo ADMIN y ALMACENERO pueden modificar el estado. El VENDEDOR solo puede crear pedidos, no cambiar estado.
- **Backend**: Migrar pedidos de `estado: str` a `estado_id: int` FK → `estados_pedido(id)`. El schema Pydantic de Pedido cambia su campo `estado` por `estado_id`.
- **Backend**: Nuevo repositorio `estado_repository.py` para consultar `estados_pedido`.
- **Frontend**: Ocultar el control de cambio de estado (select/dropdown) cuando el usuario logueado es VENDEDOR.
- **Frontend**: Ajustar modelo `Pedido` para usar `estadoId` en lugar de `estado`.
- **Base de datos**: Migrar de 7 a 15 tablas con relaciones completas (roles, estados_pedido, categorias, etc.). **BREAKING**: Cambio de esquema de base de datos.

## Capabilities

### New Capabilities
- `pedido-estado-permisos`: Control de permisos sobre modificación de estado de pedidos. Especifica qué roles pueden cambiar estado y cómo se valida tanto en backend como en frontend.
- `esquema-estados-pedido`: Migración del esquema de base de datos para normalizar estados de pedido y otras entidades maestras (roles, categorias, ubicaciones).

### Modified Capabilities
- (ninguna — no hay specs previas en este proyecto que modificar)

## Impact

- **Backend**: `pedido_api.py` (nueva validación de rol en PUT), `pedido_service.py` (validación de estado), `pedido_repository.py` (uso de estado_id), nuevo `estado_repository.py`, `esquema/pedido.py` (estado → estado_id)
- **Frontend**: `pedido-component.ts` (ocultar selector de estado para VENDEDOR), `models/pedido.model.ts` (estado → estadoId)
- **Base de datos**: 8 nuevas tablas creadas en Supabase (roles, estados_pedido, categorias, estados_producto, ordenes_compra, orden_compra_detalles, proveedor_productos, ubicaciones_locales, ubicaciones_nacionales)
- **Sin cambios**: estructura de carpetas, login, sidebar, guards

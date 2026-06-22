## Why

El sistema actual tiene 7 tablas planas sin normalización de entidades maestras. Los roles son texto libre, los estados de pedido y producto son strings sin control, y no hay relación entre proveedores y productos ni ubicaciones geográficas. Esto impide implementar reglas de negocio como "solo ADMIN y ALMACENERO cambian estado de pedidos" o "control de stock por categoría". Se requiere migrar a un esquema de 15 tablas con relaciones FK completas para dar soporte a un flujo ERP real.

## What Changes

### Base de Datos — **BREAKING**
- Migrar `usuarios.rol` (texto) → `usuarios.rol_id` (FK → `roles.id`)
- Migrar `productos.estado` (texto) → `productos.estado_id` (FK → `estados_producto.id`)
- Migrar `pedidos.estado` (texto) → `pedidos.estado_id` (FK → `estados_pedido.id`)
- Migrar `clientes` y `proveedores` para incluir FK a `ubicaciones_locales` y `ubicaciones_nacionales`
- Agregar `productos.categoria_id` (FK → `categorias.id`)
- Crear tablas de compras extendidas: `ordenes_compra`, `orden_compra_detalles`, `proveedor_productos`

### Backend (FastAPI)
- Adaptar schemas Pydantic a nuevas relaciones (campos texto → IDs)
- Validar permisos de cambio de estado: solo ADMIN y ALMACENERO en `PUT /pedidos/{id}`
- Nuevo endpoint/repo: `estado_repository`, `categoria_repository`, `ubicacion_repository`
- Adaptar `usuario_repository` para usar `rol_id` en lugar de `rol` texto

### Frontend (Angular)
- Adaptar modelos TypeScript a nuevas entidades
- Ocultar controles de estado según rol del usuario
- Ajustar servicios HTTP para enviar/recibir IDs en lugar de strings

## Capabilities

### New Capabilities
- `roles-permisos`: Sistema de roles normalizado con tabla `roles` y FK desde `usuarios`. Control de acceso basado en `rol_id`.
- `estados-pedido-flujo`: Manejo de estados de pedidos mediante `estados_pedido` con FK. Solo ADMIN y ALMACENERO pueden transicionar estados.
- `estados-producto-catalogo`: Estados de producto normalizados (ACTIVO, INACTIVO, etc.) mediante `estados_producto`.
- `categorias-productos`: Clasificación de productos por categorías mediante `categorias` y FK en `productos`.
- `ubicaciones-geograficas`: Gestión de ubicaciones locales (clientes) y nacionales (proveedores) con tablas separadas.
- `compras-extendidas`: Módulo de compras con `ordenes_compra`, `orden_compra_detalles` y `proveedor_productos` para precios sugeridos.

### Modified Capabilities
- (ninguna — proyecto sin specs previas)

## Impact

### Archivos a crear (Backend)
- `esquema/rol.py`, `repositorio/rol_repository.py`
- `esquema/estado_pedido.py`, `repositorio/estado_pedido_repository.py`
- `esquema/estado_producto.py`, `repositorio/estado_producto_repository.py`
- `esquema/categoria.py`, `repositorio/categoria_repository.py`
- `esquema/ubicacion_local.py`, `esquema/ubicacion_nacional.py`
- `repositorio/ubicacion_repository.py`
- `esquema/orden_compra.py`, `repositorio/orden_compra_repository.py`
- `repositorio/proveedor_producto_repository.py`

### Archivos a modificar (Backend)
- `esquema/usuario.py` (rol → rol_id)
- `esquema/producto.py` (estado → estado_id, + categoria_id)
- `esquema/pedido.py` (estado → estado_id)
- `esquema/cliente.py` (+ ubicacion_local_id)
- `esquema/proveedor.py` (+ ubicacion_nacional_id)
- `esquema/compra.py` (→ orden_compra)
- `apis/pedido_api.py` (validación de permisos)
- `apis/usuario_api.py` (adaptar a rol_id)
- `servicios/pedido_service.py` (validar rol en actualizar)
- `servicios/usuario_service.py` (verificar_login con rol_id)
- `repositorio/usuario_repository.py` (rol_id)
- `repositorio/pedido_repository.py` (estado_id)
- `repositorio/producto_repository.py` (estado_id, categoria_id)

### Archivos a modificar (Frontend)
- `models/usuario.model.ts`
- `models/producto.model.ts`
- `models/pedido.model.ts`
- `models/cliente.model.ts`
- `models/proveedor.model.ts`
- `features/pedido-component/pedido-component.ts` (ocultar estado si VENDEDOR)
- `features/pedido-component/pedido-component.html`

### Fases de migración
| Fase | Tablas | Depende de |
|---|---|---|
| 1 | roles, usuarios.rol_id, estados_pedido, pedidos.estado_id | — |
| 2 | categorias, estados_producto, productos.categoria_id + estado_id | Fase 1 |
| 3 | ubicaciones_locales, ubicaciones_nacionales, clientes + proveedores con FK | Fase 2 |
| 4 | ordenes_compra, orden_compra_detalles, proveedor_productos | Fase 3 |

## ADDED Requirements

### Requirement: Tabla ordenes_compra
El sistema SHALL tener una tabla `ordenes_compra` para gestionar las órdenes de compra a proveedores, reemplazando la tabla `compras` actual.

#### Scenario: Tabla ordenes_compra creada
- **WHEN** se ejecuta la migración Fase 4
- **THEN** la tabla `ordenes_compra` SHALL existir con: `id` (PK), `proveedor_id` (BIGINT FK → proveedores.id), `fecha_emision` (TIMESTAMPTZ), `total` (NUMERIC), `created_at` (TIMESTAMPTZ)

### Requirement: Tabla orden_compra_detalles
El sistema SHALL tener una tabla `orden_compra_detalles` para los items de cada orden de compra.

#### Scenario: Tabla orden_compra_detalles creada
- **WHEN** se ejecuta la migración Fase 4
- **THEN** `orden_compra_detalles` SHALL existir con: `id` (PK), `orden_compra_id` (BIGINT FK → ordenes_compra.id), `producto_id` (BIGINT FK → productos.id), `cantidad` (INTEGER), `precio_unitario` (NUMERIC), `subtotal` (NUMERIC)

### Requirement: Tabla proveedor_productos
El sistema SHALL tener una tabla `proveedor_productos` para relacionar proveedores con productos y precios sugeridos.

#### Scenario: Tabla proveedor_productos creada
- **WHEN** se ejecuta la migración Fase 4
- **THEN** `proveedor_productos` SHALL existir con: `id` (PK), `proveedor_id` (BIGINT FK → proveedores.id), `producto_id` (BIGINT FK → productos.id), `precio_sugerido` (NUMERIC), UNIQUE(proveedor_id, producto_id)

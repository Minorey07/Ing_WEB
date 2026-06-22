## ADDED Requirements

### Requirement: Tabla estados_pedido
La base de datos SHALL contener una tabla `estados_pedido` con los estados válidos para el ciclo de vida de un pedido.

#### Scenario: Tabla estados_pedido creada
- **WHEN** se ejecuta el script de migración
- **THEN** la tabla `estados_pedido` SHALL existir con columnas: `id` (PK), `nombre` (TEXT UNIQUE), `descripcion` (TEXT)
- **AND** SHALL contener al menos 2 registros: `(1, 'PENDIENTE')` y `(2, 'ENTREGADO')`

### Requirement: Tabla roles
La base de datos SHALL contener una tabla `roles` para normalizar el campo `rol` de la tabla `usuarios`.

#### Scenario: Tabla roles creada
- **WHEN** se ejecuta el script de migración
- **THEN** la tabla `roles` SHALL existir con columnas: `id` (PK), `nombre` (TEXT UNIQUE)
- **AND** SHALL contener 3 registros: `(1, 'ADMIN')`, `(2, 'ALMACENERO')`, `(3, 'VENDEDOR')`

### Requirement: Migración de pedidos.estado a pedidos.estado_id
La tabla `pedidos` SHALL reemplazar la columna `estado` (TEXT) por `estado_id` (BIGINT FK → estados_pedido.id).

#### Scenario: Columna estado_id en pedidos
- **WHEN** se ejecuta la migración
- **THEN** la tabla `pedidos` SHALL tener `estado_id BIGINT NOT NULL REFERENCES estados_pedido(id)`
- **AND** la columna `estado` (TEXT) SHALL ser eliminada

### Requirement: Tablas maestras adicionales
La base de datos SHALL incluir tablas maestras para normalizar categorias, estados de producto y ubicaciones.

#### Scenario: Tablas maestras creadas
- **WHEN** se ejecuta el script de migración
- **THEN** SHALL existir: `categorias`, `estados_producto`, `ubicaciones_locales`, `ubicaciones_nacionales`
- **AND** cada una SHALL tener columna `id` (PK) y `nombre` (TEXT)

### Requirement: Tablas de compras extendidas
La base de datos SHALL incluir tablas para el módulo de compras con `ordenes_compra`, `orden_compra_detalles` y `proveedor_productos`.

#### Scenario: Tablas de compras creadas
- **WHEN** se ejecuta el script de migración
- **THEN** SHALL existir `ordenes_compra` con FK a `proveedores`
- **AND** SHALL existir `orden_compra_detalles` con FK a `ordenes_compra` y `productos`
- **AND** SHALL existir `proveedor_productos` con FK a `proveedores` y `productos`

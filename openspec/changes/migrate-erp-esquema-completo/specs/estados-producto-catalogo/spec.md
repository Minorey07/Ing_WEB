## ADDED Requirements

### Requirement: Tabla estados_producto
El sistema SHALL tener una tabla `estados_producto` que contenga los estados válidos para productos.

#### Scenario: Tabla estados_producto creada
- **WHEN** se ejecuta la migración Fase 2
- **THEN** la tabla `estados_producto` SHALL existir con `id` (PK), `nombre` (TEXT UNIQUE)
- **AND** SHALL contener: `(1, 'ACTIVO')`, `(2, 'INACTIVO')`

### Requirement: productos.estado_id reemplaza productos.estado
La tabla `productos` SHALL usar `estado_id` (FK) en lugar del campo texto `estado`.

#### Scenario: Columna estado_id en productos
- **WHEN** se ejecuta la migración Fase 2
- **THEN** `productos.estado_id` (BIGINT FK → estados_producto.id) SHALL existir
- **AND** `productos.estado` (TEXT) SHALL ser eliminada

### Requirement: Solo ADMIN y ALMACENERO modifican stock
El backend SHALL validar que solo ADMIN y ALMACENERO puedan modificar `productos.stock`. VENDEDOR solo puede leer productos.

#### Scenario: VENDEDOR intenta actualizar producto
- **WHEN** usuario con rol VENDEDOR hace PUT /productos/{id}
- **THEN** backend SHALL responder HTTP 403

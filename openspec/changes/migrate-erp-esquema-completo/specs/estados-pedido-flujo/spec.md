## ADDED Requirements

### Requirement: Tabla estados_pedido
El sistema SHALL tener una tabla `estados_pedido` que contenga los estados válidos para el ciclo de vida de un pedido.

#### Scenario: Tabla estados_pedido creada
- **WHEN** se ejecuta la migración Fase 1
- **THEN** la tabla `estados_pedido` SHALL existir con `id` (PK), `nombre` (TEXT UNIQUE)
- **AND** SHALL contener: `(1, 'PENDIENTE')`, `(2, 'ENTREGADO')`

### Requirement: pedidos.estado_id reemplaza pedidos.estado
La tabla `pedidos` SHALL usar `estado_id` (FK) en lugar del campo texto `estado`.

#### Scenario: Columna estado_id creada
- **WHEN** se ejecuta la migración
- **THEN** `pedidos.estado_id` (BIGINT FK → estados_pedido.id) SHALL existir
- **AND** `pedidos.estado` (TEXT) SHALL ser eliminada

### Requirement: Solo ADMIN y ALMACENERO pueden cambiar estado
El backend SHALL validar que solo los roles ADMIN (rol_id=1) y ALMACENERO (rol_id=2) puedan modificar el `estado_id` de un pedido. VENDEDOR (rol_id=3) SHALL recibir HTTP 403.

#### Scenario: VENDEDOR rechazado al cambiar estado
- **WHEN** usuario con rol_id=3 hace PUT /pedidos/{id}
- **THEN** backend SHALL responder HTTP 403 Forbidden

#### Scenario: Al crear pedido se asigna estado_id por defecto
- **WHEN** se crea un pedido via POST /pedidos/
- **THEN** el sistema SHALL asignar `estado_id = 1` (PENDIENTE) automáticamente

### Requirement: Frontend oculta control de estado al VENDEDOR
El frontend SHALL ocultar el selector de estado cuando el usuario logueado tenga rol VENDEDOR.

#### Scenario: VENDEDOR en página de pedidos
- **WHEN** el usuario autenticado es VENDEDOR
- **THEN** el `<select>` de estado SHALL estar oculto
- **AND** el estado se envía como `estado_id = 1` al crear

## ADDED Requirements

### Requirement: Endpoint dedicado para cambio de estado
El sistema DEBE exponer `PUT /pedidos/{id}/estado` que recibe únicamente `{estado_id: number}` y actualiza el campo `estado_id` del pedido.

#### Scenario: Cambio de estado exitoso
- **WHEN** se invoca `PUT /pedidos/1/estado` con `{"estado_id": 2}`
- **THEN** el pedido con `id=1` queda con `estado_id=2`

#### Scenario: Estado final no permite edición
- **WHEN** se invoca `PUT /pedidos/1/estado` y el pedido tiene `estado_id >= 2`
- **THEN** el sistema responde con HTTP 400 y error "El pedido ya tiene un estado final"

### Requirement: Validación de rol para cambio de estado
El sistema DEBE rechazar cambios de estado si el usuario autenticado no tiene rol ADMIN(1) o ALMACENERO(2).

#### Scenario: VENDEDOR intenta cambiar estado
- **WHEN** un usuario con `rol_id=3` (VENDEDOR) invoca `PUT /pedidos/1/estado`
- **THEN** el sistema responde con HTTP 403

#### Scenario: ADMIN cambia estado exitosamente
- **WHEN** un usuario con `rol_id=1` (ADMIN) invoca `PUT /pedidos/1/estado`
- **THEN** el sistema actualiza el estado correctamente

### Requirement: Frontend oculta control de estado para VENDEDOR
El frontend NO DEBE mostrar el selector de estado en el formulario de pedidos cuando el usuario logueado tiene `rol_id=3`.

#### Scenario: VENDEDOR no ve selector
- **WHEN** `rolId === 3`
- **THEN** el `<select>` de estado no se renderiza

#### Scenario: ADMIN ve selector
- **WHEN** `rolId !== 3`
- **THEN** el `<select>` de estado se renderiza normalmente

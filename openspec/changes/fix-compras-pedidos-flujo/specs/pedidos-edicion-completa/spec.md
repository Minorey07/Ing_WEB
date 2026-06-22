## ADDED Requirements

### Requirement: Editar pedido completo
El sistema DEBE permitir editar `cliente_id`, productos y total de un pedido existente.

#### Scenario: ADMIN edita pedido
- **WHEN** ADMIN invoca `PUT /pedidos/{id}` con nuevos `cliente_id` y `detalles`
- **THEN** el pedido se actualiza correctamente

#### Scenario: ALMACENERO edita pedido
- **WHEN** ALMACENERO invoca `PUT /pedidos/{id}`
- **THEN** el pedido se actualiza (puede editar productos)

#### Scenario: VENDEDOR edita pedido
- **WHEN** VENDEDOR invoca `PUT /pedidos/{id}`
- **THEN** recibe HTTP 403

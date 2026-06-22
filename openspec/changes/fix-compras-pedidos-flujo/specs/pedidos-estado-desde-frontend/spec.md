## ADDED Requirements

### Requirement: Respetar estado_id al crear pedido
El sistema DEBE respetar el `estado_id` enviado por el frontend al crear un pedido.

#### Scenario: Crear pedido con estado específico
- **WHEN** se invoca `POST /pedidos/` con `estado_id: 2`
- **THEN** el pedido se crea con `estado_id = 2` en lugar de forzar 1

#### Scenario: Crear pedido sin estado
- **WHEN** se invoca `POST /pedidos/` sin `estado_id`
- **THEN** el pedido se crea con `estado_id = 1` (PENDIENTE) por defecto

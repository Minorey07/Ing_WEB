## Why

Compras no muestran los productos dentro de cada compra. Pedidos no permiten editar existentes. El estado de pedidos se fuerza a PENDIENTE ignorando lo que envía el frontend.

## What Changes

- **Compras**: `GET /compras/` incluye `detalles` (productoNombre, cantidad, precio, subtotal) vía JOIN con compra_detalles + productos
- **Pedidos**: Habilitar `PUT /pedidos/{id}` para editar cliente_id, productos y total
- **Pedidos**: Respetar `estado_id` enviado en POST en lugar de forzar 1

## Capabilities

### New Capabilities
- `compras-con-detalles`: endpoint de compras enriquecido con lista de productos comprados
- `pedidos-edicion-completa`: PUT /pedidos/{id} permite editar cabecera y productos
- `pedidos-estado-desde-frontend`: POST /pedidos/ respeta estado_id enviado

## Impact

- Backend: compra_repository, pedido_service, pedido_api
- Frontend: compra-component, pedido-component

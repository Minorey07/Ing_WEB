## Why

Los módulos de compras, compra_detalles y pedidos en Melius SAC muestran solo IDs numéricos sin contexto (proveedor_id, producto_id, estado_id), lo que obliga al usuario a memorizar o consultar referencias externas. Además, no existe control de flujo de estados en pedidos ni actualización automática de stock al registrar compras. Estas carencias afectan la usabilidad y la integridad del inventario.

## What Changes

- **Compras**: enriquecer el listado con `proveedor_nombre` (razón social) mediante JOIN con proveedores
- **Compra_detalles**: enriquecer el listado con `producto_nombre` mediante JOIN con productos
- **Compra_detalles**: al registrar un detalle, incrementar automáticamente `productos.stock += cantidad`
- **Pedidos**: nuevo endpoint `PUT /pedidos/{id}/estado` que solo actualiza `estado_id`
- **Pedidos**: validar rol (solo ADMIN y ALMACENERO pueden cambiar estado)
- **Pedidos**: bloquear edición si el estado actual es final (ENTREGADO=2, futuro CANCELADO)
- **Frontend**: mostrar nombres en lugar de IDs en compras, compra_detalles y pedidos

## Capabilities

### New Capabilities
- `compras-enriquecidas`: listado de compras con nombre del proveedor integrado
- `compra-detalles-enriquecidos`: listado de compra_detalles con nombre del producto y auto-stock
- `pedidos-control-estados`: endpoint dedicado para cambio de estado con validación por rol y estado final

### Modified Capabilities
*(ninguna — no existen specs previas)*

## Impact

- **Backend**: repositorios de compras, compra_detalles, pedidos + nuevos servicios/schemas minimales
- **Frontend**: modelos TypeScript, componentes de compras y compra_detalles para mostrar nombres
- **Base de datos**: sin cambios de schema — solo se usan JOINs sobre tablas existentes
- **No hay breaking changes**: endpoints existentes siguen funcionando; se agrega `PUT /pedidos/{id}/estado`

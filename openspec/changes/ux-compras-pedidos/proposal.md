## Why

La UI de compras y pedidos muestra información técnica (razón social, IDs) en lugar de nombres legibles. El carrito de pedidos no tiene formato de tabla clara.

## What Changes

- Pedidos: carrito en formato tabla con nombre, cantidad, precio, subtotal
- Compras: alias `razon_social` → `proveedor_nombre` en JOIN, label "Nombre del proveedor"
- Proveedores: selects muestran solo nombre legible

## Impact

Frontend templates y labels. Sin cambios de backend lógico.

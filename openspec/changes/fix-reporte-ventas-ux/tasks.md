# Tasks: Fix Reporte de Ventas UX

## 1. Backend — JOIN clientes y usuarios en pedido_repository

- [x] 1.1 Agregar JOIN `clientes!inner(nombres)` y `usuarios!inner(nombre)` en `pedido_repository.listar()` para retornar `cliente_nombre` y `vendedor_nombre`

## 2. Frontend — Modelo Pedido con nombres

- [x] 2.1 Agregar campos `clienteNombre` y `vendedorNombre` a la interfaz `Pedido`

## 3. Frontend — Reporte de Ventas sin fecha y con nombres

- [x] 3.1 Reemplazar `clienteId` / `vendedorId` por `clienteNombre` / `vendedorNombre` en la tabla
- [x] 3.2 Eliminar columna Fecha del reporte
- [x] 3.3 Agregar botón expandible para mostrar detalle de productos (nombre, cantidad, precio, subtotal)

## 4. Verificación

- [x] 4.1 `ng build` sin errores TS

# Tasks: Fix Compras, Pedidos Edición y Estado

## 1. Compras — Detalles anidados en listado

- [x] 1.1 Modificar `compra_repository.listar()` para incluir `detalles[]` con JOIN a `compra_detalles` + `productos`
- [x] 1.2 Actualizar `esquema/compra.py` para incluir campo `detalles: list[CompraDetalle]`
- [x] 1.3 Actualizar `compra-component.html` para mostrar tabla expandible de productos por compra

## 2. Pedidos — Edición habilitada

- [x] 2.1 Modificar `pedido_service.actualizar()` — ADMIN/VENDEDOR editan, ALMACENERO solo vía endpoint estado
- [x] 2.2 Frontend: botón Editar en tabla, vendedorId dinámico desde authService

## 3. Pedidos — Estado respetado en creación

- [x] 3.1 Modificar `pedido_service.crear()` — respeta `estado_id` del frontend, no fuerza 1
- [x] 3.2 Frontend ya envía `estadoId` como number desde `modeloPedido().estadoId`

## 4. Verificación

- [x] 4.1 `GET /compras/` — `compra_repository.listar()` incluye detalles con JOIN
- [x] 4.2 `PUT /pedidos/{id}` — `pedido_service.actualizar()` permite ADMIN/VENDEDOR, bloquea ALMACENERO
- [x] 4.3 `POST /pedidos/` — `pedido_service.crear()` ya no fuerza estado_id=1
- [x] 4.4 `ng build` sin errores TS

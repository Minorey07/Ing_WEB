## Context

Actualmente `pedidos.estado` es texto libre (`PENDIENTE` | `ENTREGADO`), y cualquier rol (ADMIN, ALMACENERO, VENDEDOR) puede modificarlo mediante `PUT /pedidos/{id}`. No hay validación en backend ni restricción visual en frontend. Se requiere migrar a `estado_id` con FK a `estados_pedido` y restringir permisos para que solo ADMIN y ALMACENERO puedan cambiar estado.

## Goals / Non-Goals

**Goals:**
- Backend rechaza cambio de estado si el rol es VENDEDOR (HTTP 403)
- Frontend oculta el selector de estado al VENDEDOR
- `pedidos.estado` migra a `pedidos.estado_id` con FK a `estados_pedido`
- Se crean tablas maestras: `estados_pedido`, `roles`, `categorias`, `estados_producto`, `ubicaciones_locales`, `ubicaciones_nacionales`
- Se crean tablas de compras extendidas: `ordenes_compra`, `orden_compra_detalles`, `proveedor_productos`
- El endpoint `POST /pedidos/` asigna automáticamente `estado_id = 1` (PENDIENTE)

**Non-Goals:**
- No se migran datos existentes de la tabla `pedidos` (se asume BD nueva)
- No se modifica login, sidebar, guards, ni estructura de carpetas
- No se agregan nuevas dependencias

## Decisions

### Decision 1: Validación de permisos en `pedido_service.py`
Se agrega un parámetro `current_user: dict` a `pedido_service.actualizar()`. Si `current_user["rol"] == "VENDEDOR"`, se lanza `ValueError("No autorizado para cambiar estado")`.

**Alternativa**: Crear un endpoint separado `PUT /pedidos/{id}/estado`. Descartado porque sobrecarga la API. La validación en el servicio existente es más simple.

### Decision 2: `estado_id` se asigna automáticamente al crear
`pedido_service.crear()` asigna `estado_id = 1` (PENDIENTE) automáticamente, ignorando cualquier valor enviado por el frontend. El VENDEDOR no puede definir el estado inicial.

**Alternativa**: Permitir que el frontend envíe estado_id. Descartado porque contradice la regla de negocio: el estado lo controla ADMIN/ALMACENERO, no VENDEDOR.

### Decision 3: Frontend condiciona el selector de estado por rol
El template `pedido-component.html` usa `*ngIf` para mostrar/ocultar el `<select>` de estado según `authService.getRol() !== 'VENDEDOR'`.

**Alternativa**: Crear dos templates separados. Descartado por sobreingeniería para un solo campo condicional.

### Decision 4: El modelo `Pedido` en frontend usa `estadoId` en lugar de `estado`
Se actualiza `models/pedido.model.ts` para reflejar la nueva estructura: `estadoId: number` en lugar de `estado: string`. El nombre del estado se obtiene mediante lookup local o JOIN.

**Alternativa**: Mantener `estado` como string y convertir internamente. Descartado porque oculta el cambio de esquema y puede causar inconsistencias.

## Risks / Trade-offs

| Riesgo | Mitigación |
|---|---|
| Frontend existente espera `estado` string, puede romperse al recibir `estado_id` | El endpoint `GET /pedidos/` debe devolver también `estado_nombre` (obtenido vía JOIN o lookup) |
| VENDEDOR no puede ver el estado actual del pedido | El VENDEDOR SÍ puede VER el estado (como badge de solo lectura), solo no puede EDITARLO |
| Migración de BD existente (si hay datos) pierde los estados actuales | Se asume BD nueva. Si hay datos, script SQL debe migrar: `UPDATE pedidos SET estado_id = CASE estado WHEN 'PENDIENTE' THEN 1 WHEN 'ENTREGADO' THEN 2 END` |
| El endpoint PUT actual acepta cualquier campo del pedido, no solo estado | Se mantiene PUT completo pero se valida el permiso. Si solo cambia estado, el frontend puede seguir enviando el objeto completo. |

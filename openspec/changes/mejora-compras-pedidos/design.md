## Context

Melius SAC tiene tablas existentes `compras`, `compra_detalles`, `pedidos`, `proveedores`, `productos`, `estados_pedido` con relaciones FK en Supabase. Actualmente los repositorios hacen `SELECT *` sin JOINs, por lo que el frontend recibe solo IDs numéricos. No existe actualización automática de stock y los pedidos carecen de control de flujo de estados.

## Goals / Non-Goals

**Goals:**
- Enriquecer `GET /compras/` con `proveedor_nombre` vía JOIN
- Enriquecer `GET /compra-detalles/` con `producto_nombre` vía JOIN
- Incrementar `productos.stock` automáticamente al crear `compra_detalles`
- Exponer `PUT /pedidos/{id}/estado` solo para cambiar `estado_id`
- Validar rol: solo ADMIN(1) y ALMACENERO(2) pueden cambiar estado de pedido
- Bloquear cambio de estado si el estado actual del pedido es 2 (ENTREGADO) o se considera final
- Mostrar nombres (proveedor, producto, estado) en frontend Angular

**Non-Goals:**
- No crear nuevas tablas ni modificar el schema de Supabase
- No reestructurar componentes Angular existentes
- No agregar autenticación ni nuevos módulos
- No modificar `compras` ni `compra_detalles` en frontend más allá de mostrar nombres

## Decisions

1. **JOINs en repositorios, no en servicio** — Los repositorios existentes (`compra_repository`, `compra_detalle_repository`) usarán la sintaxis `!inner` de Supabase para traer nombres asociados. Esto evita capas de transformación y mantiene la data lista para la API. Alternativa considerada: hacer llamadas separadas y mergear en servicio, descartada por N+1 queries.

2. **Endpoint PUT /pedidos/{id}/estado separado** — Se crea un nuevo endpoint en vez de modificar el `PUT /pedidos/{id}` existente, para no romper la API actual. El nuevo endpoint recibe solo `{estado_id: number}` y valida rol + estado final en el servicio.

3. **Validación de estado final** — Se define que los estados con `id >= 2` son finales y no permiten edición. Esto permite que futuros estados como CANCELADO(3) se comporten como finales automáticamente.

4. **Auto-stock en servicio de compra_detalles** — Al crear un detalle de compra, el servicio invocará `producto_service.incrementar_stock(producto_id, cantidad)` para mantener consistencia. Alternativa: trigger en base de datos, descartado porque las migraciones SQL ya se aplicaron y no queremos tocar Supabase.

5. **Frontend sin nuevos componentes** — Se modificarán los templates existentes de compras y pedidos para mapear `proveedor_nombre`, `producto_nombre`, `estado_nombre` desde los modelos. No se crean vistas nuevas.

## Risks / Trade-offs

- **[Rendimiento]** JOINs `!inner` pueden fallar si un registro tiene FK nula → Mitigación: todas las FK tienen `NOT NULL` o valor por defecto después de la migración
- **[Consistencia]** El auto-stock vía Python y no vía DB trigger puede tener race conditions si hay concurrencia → Mitigación: Melius SAC es sistema monousuario académico, no aplica
- **[Frontend]** Si el backend no devuelve `proveedor_nombre`, el frontend mostrará `undefined` → Mitigación: tipar como opcional con `?` en interfaces TypeScript

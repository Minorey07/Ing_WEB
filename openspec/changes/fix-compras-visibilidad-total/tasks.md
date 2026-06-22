# Tasks: Fix Compras Visibilidad Total

## 1. Backend — Eliminar todo !inner en consultas de compras

- [x] 1.1 `compra_repository.listar()`: reemplazar `productos!inner(nombre)` por consulta separada `productos.select("nombre").eq("id", d["producto_id"])` — sin JOINs que puedan fallar por FKs faltantes
- [x] 1.2 `compra_detalle_repository.listar()`: mismo cambio — eliminar `productos!inner(nombre)` por consulta manual
- [x] 1.3 `proveedor_nombre` ya usa consulta separada desde arreglo anterior
- [x] 1.4 Eliminar `try/except` ya que ya no hay JOINs que puedan fallar
- [x] 1.5 `detalles` siempre es `[]` (nunca `None`)

## 2. Frontend — Fallbacks robustos

- [x] 2.1 `getNombreProveedor()` retorna `'Sin proveedor'` cuando no hay match (en vez de `'Proveedor #id'`)
- [x] 2.2 Template: `d.productoNombre || 'Producto no disponible'`
- [x] 2.3 Template: `compra.detalles?.length` con `@else` "Sin detalle de productos"
- [x] 2.4 Mantener console.log en `cargarCompras()` para depuración

## 3. Verificación

- [x] 3.1 `ng build` sin errores TS

# Tasks: Fix Compras Listado Vacío

## 1. Backend — Verificar JOINs en compra_repository

- [x] 1.1 Asegurar JOIN `proveedores!inner(razon_social)` en `listar()` para retornar `proveedor_nombre`
- [x] 1.2 Asegurar JOIN `productos!inner(nombre)` en detalle para retornar `producto_nombre`
- [x] 1.3 Usar variable local `compras` en lugar de `resp.data` directo (consistencia)

## 2. Frontend — Modelo Compra con createdAt

- [x] 2.1 Reemplazar `fecha: Date` por `createdAt?: string` en interfaz `Compra` (backend retorna `created_at` → `createdAt` tras camelcase-keys)

## 3. Frontend — Compra component

- [x] 3.1 Eliminar `fecha: new Date()` de `modeloCompra` — fecha la asigna Supabase automáticamente
- [x] 3.2 Template: mostrar `compra.proveedorNombre || getNombreProveedor(compra.proveedorId)` (fallback local)
- [x] 3.3 Template: mostrar `compra.createdAt | date:'short'` con `—` si no hay fecha
- [x] 3.4 Template: expand toggle siempre visible; si no hay detalles mostrar "Sin detalle de productos"
- [x] 3.5 Template: productoNombre con fallback `'Producto #' + d.productoId`

## 4. Verificación

- [x] 4.1 `ng build` sin errores TS

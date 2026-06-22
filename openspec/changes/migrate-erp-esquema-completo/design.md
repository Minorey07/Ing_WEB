# Design: Migración ERP — Esquema Completo

## 1. Database Schema (15 tables)

```
┌─────────────────────────────────────────────────────────────────────┐
│                        MELIUS SAC — 15 TABLAS                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  roles                    estados_pedido           estados_producto  │
│  ┌──────┐                ┌──────────────┐         ┌──────────────┐  │
│  │id    │◄──┐            │id            │◄──┐     │id            │◄──┐
│  │nombre│   │            │nombre        │   │     │nombre        │   │
│  └──────┘   │            └──────────────┘   │     └──────────────┘   │
│             │                               │                        │
│  usuarios   │   pedidos                     │   productos            │
│  ┌──────┐   │   ┌──────────┐               │   ┌──────────────┐     │
│  │id    │   │   │id        │               │   │id            │     │
│  │nombre│   │   │cliente_id├──┐            │   │nombre        │     │
│  │correo│   │   │vendedor_id│  │           │   │descripcion   │     │
│  │rol_id├───┘   │estado_id ├──┘            │   │precio        │     │
│  │pass  │       │total     │               │   │stock         │     │
│  └──────┘       │created_at│               │   │estado_id ├────┘     │
│                 └────┬─────┘               │   │categoria_id│        │
│                      │                     │   └──────────────┘      │
│          ┌───────────┘                     │        │                │
│          ▼                                 │        │                │
│  pedido_detalles                            │        │                │
│  ┌──────────────────┐                      │        │                │
│  │id                │                      │        │                │
│  │pedido_id         │                      │        ▼                │
│  │producto_id       │                      │  categorias             │
│  │cantidad          │                      │  ┌──────────────┐       │
│  │precio            │                      │  │id            │       │
│  │subtotal          │                      │  │nombre        │       │
│  └──────────────────┘                      │  │descripcion   │       │
│                                             │  └──────────────┘       │
│  ubicaciones_locales   clientes             │                         │
│  ┌──────────────────┐ ┌──────────────┐      │                         │
│  │id                │ │id            │      │                         │
│  │nombre            │ │nombres       │      │                         │
│  │distrito          │ │telefono      │      │                         │
│  │provincia         │ │direccion     │      │                         │
│  │departamento      │ │ubicacion_local_id│  │                         │
│  └──────────────────┘ └──────────────┘      │                         │
│                                             │                         │
│  ubicaciones_nacionales  proveedores        │                         │
│  ┌──────────────────┐ ┌──────────────┐      │                         │
│  │id                │ │id            │      │                         │
│  │nombre            │ │razon_social  │      │                         │
│  │region            │ │ruc           │      │                         │
│  │pais              │ │telefono      │      │                         │
│  └──────────────────┘ │direccion     │      │                         │
│                       │ubicacion_nac_id│    │                         │
│                       └───────┬──────┘      │                         │
│                               │             │                         │
│  ordenes_compra               │             │                         │
│  ┌──────────────────┐         │             │                         │
│  │id                │         │             │                         │
│  │proveedor_id ├────┘         │             │                         │
│  │fecha_emision    │          │             │                         │
│  │total            │          │             │                         │
│  │created_at       │          │             │                         │
│  └────┬─────────────┘         │             │                         │
│       │                      │             │                          │
│  ┌────▼──────────────┐      │             │                           │
│  │orden_compra_detalles│     │             │                           │
│  │┌──────────────────┐│     │             │                           │
│  ││id                ││     │             │                           │
│  ││orden_compra_id   ││     │             │                           │
│  ││producto_id       ││     │             │                           │
│  ││cantidad          ││     │             │                           │
│  ││precio_unitario   ││     │             │                           │
│  ││subtotal          ││     │             │                           │
│  │└──────────────────┘│     │             │                           │
│  └────────────────────┘     │             │                           │
│                              │             │                           │
│  proveedor_productos         │             │                           │
│  ┌──────────────────┐        │             │                           │
│  │id                │        │             │                           │
│  │proveedor_id  ├───┘        │             │                           │
│  │producto_id  ├─────────────┘             │                           │
│  │precio_sugerido│                         │                           │
│  └──────────────────┘                      │                           │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

### New tables (8):
| Table | Purpose | Key columns |
|-------|---------|-------------|
| `roles` | Roles del sistema | `id`, `nombre` |
| `estados_pedido` | Estados de pedido | `id`, `nombre` |
| `estados_producto` | Estados de producto | `id`, `nombre` |
| `categorias` | Categorías de producto | `id`, `nombre`, `descripcion` |
| `ubicaciones_locales` | Ubicaciones de clientes | `id`, `nombre`, `distrito`, `provincia`, `departamento` |
| `ubicaciones_nacionales` | Ubicaciones de proveedores | `id`, `nombre`, `region`, `pais` |
| `ordenes_compra` | Órdenes de compra | `id`, `proveedor_id`, `fecha_emision`, `total`, `created_at` |
| `orden_compra_detalles` | Detalles de orden de compra | `id`, `orden_compra_id`, `producto_id`, `cantidad`, `precio_unitario`, `subtotal` |
| `proveedor_productos` | Productos por proveedor | `id`, `proveedor_id`, `producto_id`, `precio_sugerido` |

### Modified tables (7):
| Table | Change |
|-------|--------|
| `usuarios` | `rol` (TEXT) → `rol_id` (BIGINT FK → roles.id) |
| `pedidos` | `estado` (TEXT) → `estado_id` (BIGINT FK → estados_pedido.id) |
| `productos` | `estado` (TEXT) → `estado_id` (BIGINT FK → estados_producto.id); + `categoria_id` (BIGINT FK → categorias.id, nullable) |
| `clientes` | + `ubicacion_local_id` (BIGINT FK → ubicaciones_locales.id, nullable) |
| `proveedores` | + `ubicacion_nacional_id` (BIGINT FK → ubicaciones_nacionales.id, nullable) |
| `compras` | Reemplazada por `ordenes_compra` + `orden_compra_detalles` |
| `pedido_detalles` | Sin cambios estructurales |

### Seed data:
```sql
-- Fase 1
INSERT INTO roles (id, nombre) VALUES (1, 'ADMIN'), (2, 'ALMACENERO'), (3, 'VENDEDOR');
INSERT INTO estados_pedido (id, nombre) VALUES (1, 'PENDIENTE'), (2, 'ENTREGADO');

-- Fase 2
INSERT INTO estados_producto (id, nombre) VALUES (1, 'ACTIVO'), (2, 'INACTIVO');
```

---

## 2. Backend Architecture Changes

### Pattern: Repository → Service → API (sin cambios estructurales)
El patrón actual se mantiene. Solo se modifican/agregan archivos dentro de cada capa.

```
FastAPI (main.py)
  │
  ├── apis/        ← Controladores HTTP
  ├── servicios/   ← Lógica de negocio
  ├── repositorio/ ← Acceso a datos (supabase-py)
  └── esquema/     ← Pydantic models
```

### Schema layer — Cambios por archivo:

| Archivo | Cambio |
|---------|--------|
| `esquema/usuario.py` | `rol: str` → `rol_id: int`; agregar `rol_nombre: str \| None` para respuestas |
| `esquema/pedido.py` | `estado: str` → `estado_id: int`; agregar `estado_nombre: str \| None` |
| `esquema/producto.py` | `estado: str` → `estado_id: int`; + `categoria_id: int \| None`; + `categoria_nombre: str \| None`, `estado_nombre: str \| None` |
| `esquema/cliente.py` | + `ubicacion_local_id: int \| None` |
| `esquema/proveedor.py` | + `ubicacion_nacional_id: int \| None` |
| `esquema/compra.py` | Reemplazar por `OrdenCompra` + `OrdenCompraDetalle` |

### New schema files:

| Archivo | Modelos |
|---------|---------|
| `esquema/rol.py` | `Rol` (id, nombre) |
| `esquema/estado_pedido.py` | `EstadoPedido` (id, nombre) |
| `esquema/estado_producto.py` | `EstadoProducto` (id, nombre) |
| `esquema/categoria.py` | `Categoria` (id, nombre, descripcion) |
| `esquema/ubicacion_local.py` | `UbicacionLocal` (id, nombre, distrito, provincia, departamento) |
| `esquema/ubicacion_nacional.py` | `UbicacionNacional` (id, nombre, region, pais) |
| `esquema/orden_compra.py` | `OrdenCompra` (id, proveedor_id, fecha_emision, total, created_at), `OrdenCompraDetalle` (id, orden_compra_id, producto_id, cantidad, precio_unitario, subtotal) |

### New repository files:

| Archivo | Métodos | TABLE |
|---------|---------|-------|
| `repositorio/rol_repository.py` | listar, crear, actualizar, eliminar | `roles` |
| `repositorio/estado_pedido_repository.py` | listar | `estados_pedido` |
| `repositorio/estado_producto_repository.py` | listar | `estados_producto` |
| `repositorio/categoria_repository.py` | listar, crear, actualizar, eliminar | `categorias` |
| `repositorio/ubicacion_repository.py` | listar_locales, crear_local, actualizar_local, eliminar_local, listar_nacionales, crear_nacional, actualizar_nacional, eliminar_nacional | `ubicaciones_locales`, `ubicaciones_nacionales` |
| `repositorio/orden_compra_repository.py` | listar, crear, actualizar, eliminar | `ordenes_compra` |
| `repositorio/proveedor_producto_repository.py` | listar, crear, actualizar, eliminar | `proveedor_productos` |

### Auth layer — cambios:

**`auth/dependencies.py`**:
- `get_current_user`: agregar `rol_id` al dict retornado (leer desde payload `rol_id`, fallback a lookup si no existe)
- `require_roles`: aceptar tanto `rol_id` como `rol` string; dar prioridad a `rol_id`

**`auth/jwt_handler.py`**:
- `crear_token`: incluir `rol_id` en el payload JWT además de `rol`

### API layer — cambios por endpoint:

| Endpoint | Cambio |
|----------|--------|
| `PUT /pedidos/{id}` | Validar que solo ADMIN (rol_id=1) y ALMACENERO (rol_id=2) puedan cambiar `estado_id` |
| `PUT /productos/{id}` | Validar que VENDEDOR (rol_id=3) no pueda modificar stock ni estado |
| `GET /pedidos/` | Retornar `estado_id` + `estado_nombre` (join con estados_pedido) |
| `GET /productos/` | Retornar `estado_id` + `estado_nombre`, `categoria_id` + `categoria_nombre` |

### Service layer — cambios:

| Servicio | Cambio |
|----------|--------|
| `pedido_service.py` | En `actualizar`: recibir `rol_id` como parámetro, retornar 403 si no es ADMIN/ALMACENERO. En `crear`: asignar `estado_id=1` por defecto |
| `usuario_service.py` | `verificar_login`: lookup de `rol_id` y retornarlo en el token |
| `producto_service.py` | En `actualizar`: validar si quien llama es VENDEDOR → rechazar |

---

## 3. Frontend Architecture Changes

### Models — cambios por interfaz:

| Interfaz | Cambio |
|----------|--------|
| `usuario.model.ts` | `rol` → `rolId: number`; + `rolNombre: string` |
| `pedido.model.ts` | `estado` → `estadoId: number`; + `estadoNombre: string` |
| `producto.model.ts` | `estado` → `estadoId: number`; + `estadoNombre: string`; + `categoriaId?: number`; + `categoriaNombre?: string` |
| `cliente.model.ts` | + `ubicacionLocalId?: number` |
| `proveedor.model.ts` | + `ubicacionNacionalId?: number` |
| `compra.model.ts` | Reemplazar por interfaces `OrdenCompra` y `OrdenCompraDetalle` |

### New model files:
- `rol.model.ts`
- `estado-pedido.model.ts`
- `estado-producto.model.ts`
- `categoria.model.ts`
- `ubicacion-local.model.ts`
- `ubicacion-nacional.model.ts`
- `proveedor-producto.model.ts`

### Component changes:

**`pedido-component.ts`**:
- Inyectar `AuthService` para obtener `rol_id`
- Si `rol_id === 3` (VENDEDOR): ocultar selector de estado, forzar `estadoId = 1` al crear
- Si `rol_id === 1 || rol_id === 2`: mostrar selector con opciones de `estados_pedido`

**`pedido-component.html`**:
- Envolver `<select>` de estado en `@if (rol !== 'VENDEDOR')` (o usar `rol_id !== 3`)

**`dashboard-home.ts`**:
- Adaptar filtros de estado para usar `estadoId` en lugar de string

---

## 4. Security Design

### JWT Token structure (nuevo):
```json
{
  "sub": 1,
  "rol": "ADMIN",
  "rol_id": 1,
  "exp": 1719000000
}
```

### Permission matrix by operation:

| Operación | ADMIN | ALMACENERO | VENDEDOR |
|-----------|-------|------------|----------|
| CRUD Usuarios | ✅ | ❌ | ❌ |
| CRUD Productos | ✅ | ✅ | ✅ (solo lectura) |
| CRUD Pedidos (crear/leer) | ✅ | ✅ | ✅ |
| Cambiar estado pedido | ✅ | ✅ | ❌ |
| CRUD Clientes | ✅ | ✅ | ✅ |
| CRUD Proveedores | ✅ | ✅ | ❌ |
| CRUD Compras | ✅ | ✅ | ❌ |
| Dashboard (todos los datos) | ✅ | parcial | parcial |

### Validation strategy:
- Backend: `require_roles` dependency con `rol_id` para endpoints críticos
- Frontend: ocultar UI elements según `rol_id` (UX, no seguridad)
- Doble validación: frontend oculta, backend rechaza

---

## 5. Migration Strategy: Progressive 4-Phase

```
Fase 1 ─────────────────────────────────────
Roles + Estados Pedido + Usuarios/Pedidos FK
         │
         ▼
Fase 2 ─────────────────────────────────────
Categorías + Estados Producto + Productos FK
         │
         ▼
Fase 3 ─────────────────────────────────────
Ubicaciones + Clientes/Proveedores FK
         │
         ▼
Fase 4 ─────────────────────────────────────
Compras extendidas (órdenes + detalles + proveedor_productos)
```

### Rollback plan por fase:
- Cada fase tiene su propio script SQL reversible
- Fase 1 rollback: restaurar `usuarios.rol` como texto + `pedidos.estado` como texto, eliminar tablas nuevas
- Fase 2 rollback: restaurar `productos.estado` como texto, eliminar `categorias` y `estados_producto`
- Fase 3 rollback: eliminar FK columns de clientes/proveedores, eliminar tablas de ubicaciones
- Fase 4 rollback: eliminar `ordenes_compra`, `orden_compra_detalles`, `proveedor_productos`

---

## 6. Key Design Decisions

| Decisión | Opción elegida | Alternativa descartada | Razón |
|----------|---------------|----------------------|-------|
| Tipo FK | `BIGINT` | `INTEGER` | Consistencia con IDs existentes en Supabase |
| nullable categoría/cliente/proveedor FK | `NULL` permitido | `NOT NULL` | Migración progresiva, datos existentes pueden no tener categoría/ubicación |
| `rol_nombre` en response | Join en query | Cargar por separado | Minimiza llamadas a DB, el nombre es dato pequeño |
| `compras` → `ordenes_compra` | Tabla nueva | Modificar `compras` | Schema incompatible (falta proveedor_id fijo, no hay detalles) |
| Seed data | SQL inserts | API endpoints | Datos de sistema necesarios antes de que la API funcione |

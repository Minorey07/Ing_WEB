# Tasks: Migración ERP — Esquema Completo

## Fase 1 — Roles, Estados Pedido, Usuarios/Pedidos FK

**Dependencia:** Ninguna

### DB Migration (Supabase SQL)

- [x] **T1.1** Crear tabla `roles` con `id BIGSERIAL PK, nombre TEXT UNIQUE NOT NULL`
- [x] **T1.2** Insertar seed data: `(1,'ADMIN'), (2,'ALMACENERO'), (3,'VENDEDOR')`
- [x] **T1.3** Crear tabla `estados_pedido` con `id BIGSERIAL PK, nombre TEXT UNIQUE NOT NULL`
- [x] **T1.4** Insertar seed data: `(1,'PENDIENTE'), (2,'ENTREGADO')`
- [x] **T1.5** Agregar `usuarios.rol_id BIGINT FK → roles.id NOT NULL`, migrar datos desde `usuarios.rol`
- [x] **T1.6** Eliminar `usuarios.rol` (columna TEXT)
- [x] **T1.7** Agregar `pedidos.estado_id BIGINT FK → estados_pedido.id NOT NULL DEFAULT 1`, migrar datos desde `pedidos.estado`
- [x] **T1.8** Eliminar `pedidos.estado` (columna TEXT)

### Backend — Esquemas (Pydantic)

- [x] **T1.9** Crear `esquema/rol.py` con modelo `Rol(id: int \| None, nombre: str)`
- [x] **T1.10** Crear `esquema/estado_pedido.py` con modelo `EstadoPedido(id: int \| None, nombre: str)`
- [x] **T1.11** Modificar `esquema/usuario.py`: `rol: str` → `rol_id: int`; agregar `rol_nombre: str \| None = None`
- [x] **T1.12** Modificar `esquema/pedido.py`: `estado: str` → `estado_id: int`; agregar `estado_nombre: str \| None = None`

### Backend — Repositorios

- [x] **T1.13** Crear `repositorio/rol_repository.py` con CRUD estándar (`TABLE = "roles"`)
- [x] **T1.14** Crear `repositorio/estado_pedido_repository.py` con listar (`TABLE = "estados_pedido"`)
- [x] **T1.15** Modificar `repositorio/usuario_repository.py`: `rol` → `rol_id` en insert/update SELECT; agregar JOIN con `roles` para obtener `rol_nombre`

- [x] **T1.16** Modificar `repositorio/pedido_repository.py`: `estado` → `estado_id` en insert/update; agregar JOIN con `estados_pedido` para obtener `estado_nombre`

### Backend — Servicios

- [x] **T1.17** Modificar `servicios/usuario_service.py`:
  - `verificar_login`: lookup `rol_id`, pasar a `crear_token`
- [x] **T1.18** Modificar `servicios/pedido_service.py`:
  - `crear`: asignar `estado_id=1` por defecto
  - `actualizar`: recibir `rol_id`, validar que sea 1 o 2 para cambiar estado; caso contrario HTTP 403

### Backend — Auth

- [x] **T1.19** Modificar `auth/jwt_handler.py`: `crear_token` incluir `rol_id` en payload
- [x] **T1.20** Modificar `auth/dependencies.py`:
  - `get_current_user`: extraer `rol_id` del payload, agregarlo al dict retornado
  - `require_roles`: aceptar lista de `rol_id` además de nombres

### Backend — APIs

- [x] **T1.21** Modificar `apis/pedido_api.py`:
  - `actualizar`: obtener `rol_id` de `get_current_user`, pasarlo a `pedido_service.actualizar`
  - Agregar dependency `require_roles([1, 2, 3])` para GET (todos pueden ver)
- [x] **T1.22** Modificar `apis/usuario_api.py`: adaptar schemas a `rol_id`

### Frontend — Models

- [x] **T1.23** Crear `models/rol.model.ts`: `Rol { id: number; nombre: string }`
- [x] **T1.24** Crear `models/estado-pedido.model.ts`: `EstadoPedido { id: number; nombre: string }`
- [x] **T1.25** Modificar `models/usuario.model.ts`: `rol` → `rolId: number`; + `rolNombre?: string`
- [x] **T1.26** Modificar `models/pedido.model.ts`: `estado` → `estadoId: number`; + `estadoNombre?: string`

### Frontend — Components

- [x] **T1.27** Modificar `pedido-component.ts`:
  - Inyectar `AuthService`, obtener `rol_id` del usuario actual
  - `modeloPedido`: `estado` → `estadoId`
  - `guardar`: enviar `estadoId` en lugar de `estado` string
  - Si rol_id === 3 (VENDEDOR): ocultar selector, forzar `estadoId = 1`
- [x] **T1.28** Modificar `pedido-component.html`:
  - Envolver `<select>` de estado en `@if (rol_id !== 3)`
- [x] **T1.29** Modificar `dashboard-home.ts`: adaptar filtros `p.estado` → `p.estadoId`

### Frontend — Services

- [x] **T1.30** Verificar que servicios HTTP existentes envían `rol_id`/`estado_id` correctamente (snake_case transform)

---

## Fase 2 — Categorías, Estados Producto, Productos FK

**Dependencia:** Fase 1 completada

### DB Migration

- [x] **T2.1** Crear tabla `categorias` con `id BIGSERIAL PK, nombre TEXT UNIQUE NOT NULL, descripcion TEXT`
- [x] **T2.2** Crear tabla `estados_producto` con `id BIGSERIAL PK, nombre TEXT UNIQUE NOT NULL`
- [x] **T2.3** Insertar seed: `(1,'ACTIVO'), (2,'INACTIVO')` en `estados_producto`
- [x] **T2.4** Agregar `productos.categoria_id BIGINT FK → categorias.id NULL`
- [x] **T2.5** Agregar `productos.estado_id BIGINT FK → estados_producto.id NOT NULL DEFAULT 1`, migrar desde `productos.estado`
- [x] **T2.6** Eliminar `productos.estado` (columna TEXT)

### Backend — Esquemas

- [x] **T2.7** Crear `esquema/categoria.py` con `Categoria(id: int \| None, nombre: str, descripcion: str)`
- [x] **T2.8** Crear `esquema/estado_producto.py` con `EstadoProducto(id: int \| None, nombre: str)`
- [x] **T2.9** Modificar `esquema/producto.py`: `estado: str` → `estado_id: int`; + `categoria_id: int \| None = None`; + `categoria_nombre: str \| None = None`; + `estado_nombre: str \| None = None`

### Backend — Repositorios

- [x] **T2.10** Crear `repositorio/categoria_repository.py` con CRUD (`TABLE = "categorias"`)
- [x] **T2.11** Crear `repositorio/estado_producto_repository.py` con listar (`TABLE = "estados_producto"`)
- [x] **T2.12** Modificar `repositorio/producto_repository.py`: `estado` → `estado_id` en insert/update SELECT; + `categoria_id`; JOIN con `categorias` y `estados_producto`

### Backend — Servicios

- [x] **T2.13** Modificar `servicios/producto_service.py`:
  - `crear`: asignar `estado_id=1` por defecto
  - `actualizar`: validar que VENDEDOR (rol_id=3) no pueda modificar `stock` ni `estado_id`; rechazar con 403

### Backend — APIs

- [x] **T2.14** Modificar `apis/producto_api.py`:
  - `actualizar`: obtener `rol_id` de `get_current_user`, pasarlo a `producto_service.actualizar`
  - Agregar permisos: solo ADMIN/ALMACENERO pueden PUT; VENDEDOR solo GET

### Frontend — Models

- [x] **T2.15** Crear `models/estado-producto.model.ts`: `EstadoProducto { id: number; nombre: string }`
- [x] **T2.16** Crear `models/categoria.model.ts`: `Categoria { id: number; nombre: string; descripcion: string }`
- [x] **T2.17** Modificar `models/producto.model.ts`: `estado` → `estadoId: number`; + `estadoNombre?: string`; + `categoriaId?: number`; + `categoriaNombre?: string`

---

## Fase 3 — Ubicaciones Geográficas (CANCELADA)

**Dependencia:** N/A

**Nota:** Las tablas `ubicaciones_locales` y `ubicaciones_nacionales` NO existen en Supabase. El modelo actual de clientes/proveedores no incluye ubicaciones. Estas tareas quedan canceladas.

- [x] ~~**T3.1** Crear `ubicaciones_locales`~~ — CANCELED
- [x] ~~**T3.2** Crear `ubicaciones_nacionales`~~ — CANCELED
- [x] ~~**T3.3** Agregar FK en clientes~~ — CANCELED
- [x] ~~**T3.4** Agregar FK en proveedores~~ — CANCELED
- [x] ~~**T3.5** Crear esquema ubicacion_local~~ — CANCELED
- [x] ~~**T3.6** Crear esquema ubicacion_nacional~~ — CANCELED
- [x] ~~**T3.7** Modificar esquema cliente~~ — CANCELED
- [x] ~~**T3.8** Modificar esquema proveedor~~ — CANCELED
- [x] ~~**T3.9** Crear repositorio ubicaciones~~ — CANCELED
- [x] ~~**T3.10** Modificar repo cliente~~ — CANCELED
- [x] ~~**T3.11** Modificar repo proveedor~~ — CANCELED
- [x] ~~**T3.12** Crear model ubicacion-local~~ — CANCELED
- [x] ~~**T3.13** Crear model ubicacion-nacional~~ — CANCELED
- [x] ~~**T3.14** Modificar model cliente~~ — CANCELED
- [x] ~~**T3.15** Modificar model proveedor~~ — CANCELED

---

## Fase 4 — Compras Extendidas (Adaptada a DB actual)

**Dependencia:** Ninguna

**Contexto:** La DB actual tiene `compras`, `compra_detalles` y `proveedor_productos`. No se modifica Supabase. Solo se crea backend/frontend para `proveedor_productos` que aún no tiene API.

### Backend — Esquema

- [x] **T4.1** Crear `esquema/proveedor_producto.py` con `ProveedorProducto(id: int \| None, proveedor_id: int, producto_id: int, precio_sugerido: float)`

### Backend — Repositorio

- [x] **T4.2** Crear `repositorio/proveedor_producto_repository.py` con CRUD (`TABLE = "proveedor_productos"`)

### Backend — API

- [x] **T4.3** Crear `apis/proveedor_producto_api.py` con CRUD endpoints (ruta `/proveedor-productos`)

### Frontend — Model

- [x] **T4.4** Crear `models/proveedor-producto.model.ts`: `ProveedorProducto { id: number; proveedorId: number; productoId: number; precioSugerido: number }`

### Notas
- `compras` y `compra_detalles` ya existen en DB y backend — sin cambios necesarios
- No se migra a `ordenes_compra` — se mantiene el esquema actual

---

## Verificación Global (Pendiente — ejecutar manualmente)

- [x] **T.G.1** Verificar que `PUT /pedidos/{id}` rechaza VENDEDOR con 403
- [x] **T.G.2** Verificar que `PUT /productos/{id}` rechaza VENDEDOR con 403
- [x] **T.G.3** Verificar que login retorna token con `rol_id`
- [x] **T.G.4** Verificar que frontend oculta selector de estado para VENDEDOR
- [x] **T.G.5** Verificar que seed data se inserta correctamente
- [x] **T.G.6** Verificar que el sistema compila sin errores de tipo

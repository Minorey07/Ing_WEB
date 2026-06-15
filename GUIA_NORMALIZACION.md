# GUÍA DE NORMALIZACIÓN DE MODELOS

## 📋 Resumen de Cambios Realizados

Se ha implementado una **normalización completa (3FN)** de la base de datos para mejorar la organización, evitar redundancias y facilitar el mantenimiento futuro.

### ✅ Cambios en Backend (Python)

#### 1. **Nuevos Esquemas (Catálogos)**
- `categoria.py` - Tabla de categorías de productos (16 tipos)
- `estado_producto.py` - Catálogo de estados de producto (ACTIVO, AGOTADO, DESCONTINUADO, etc.)
- `estado_pedido.py` - Catálogo de estados de pedido (PENDIENTE, ENTREGADO, CANCELADO, etc.)
- `rol.py` - Catálogo de roles de usuario (ADMIN, ALMACENERO, VENDEDOR, etc.)
- `ubicacion_local.py` - Ubicaciones locales (solo Huancayo)
- `ubicacion_nacional.py` - Ubicaciones nacionales (para proveedores)

#### 2. **Esquemas Actualizados**

**usuario.py**
```python
# ANTES:
rol: str

# AHORA:
rol_id: int              # Foreign Key
rol: Optional[Rol]       # Para serialización
```

**producto.py**
```python
# ANTES:
estado: str = 'ACTIVO'

# AHORA:
categoria_id: int                    # Foreign Key
estado_id: int                       # Foreign Key
presentacion: str | None             # (ej: "Costal 50kg")
categoria: Optional[Categoria]       # Para serialización
estado: Optional[EstadoProducto]     # Para serialización
```

**cliente.py**
```python
# ANTES:
telefono: str
direccion: str

# AHORA:
ubicacion_local_id: int              # Foreign Key
ubicacion: Optional[UbicacionLocal]  # Para serialización
```

**proveedor.py**
```python
# ANTES:
telefono: str
direccion: str

# AHORA:
ubicacion_nacional_id: int                  # Foreign Key
ubicacion: Optional[UbicacionNacional]      # Para serialización
```

**pedido.py**
```python
# ANTES:
estado: str

# AHORA:
estado_id: int                  # Foreign Key
estado: Optional[EstadoPedido]  # Para serialización
```

**pedido_detalle.py**
```python
# NUEVO CAMPO:
id: int | None = None  # Clave primaria propia
```

### ✅ Cambios en Frontend (TypeScript)

#### 1. **Nuevos Modelos**
- `categoria.model.ts`
- `estado-producto.model.ts`
- `estado-pedido.model.ts`
- `rol.model.ts`
- `ubicacion-local.model.ts`
- `ubicacion-nacional.model.ts`

#### 2. **Modelos Actualizados**

**Producto**
```typescript
// ANTES:
estado: string;

// AHORA:
categoria_id: number;
estado_id: number;
presentacion?: string;
categoria?: Categoria;
estado?: EstadoProducto;
```

**Usuario**
```typescript
// ANTES:
rol: 'ADMIN' | 'ALMACENERO' | 'VENDEDOR';

// AHORA:
rol_id: number;
rol?: Rol;
```

**Cliente**
```typescript
// ANTES:
telefono: string;
direccion: string;

// AHORA:
ubicacion_local_id: number;
ubicacion?: UbicacionLocal;
```

**Proveedor**
```typescript
// ANTES:
telefono: string;
direccion: string;

// AHORA:
ubicacion_nacional_id: number;
ubicacion?: UbicacionNacional;
```

**Pedido**
```typescript
// ANTES:
estado: 'PENDIENTE' | 'ENTREGADO';

// AHORA:
estado_id: number;
estado?: EstadoPedido;
```

#### 3. **Componentes Actualizados**
- `producto-component.ts` - Ahora usa `categoria_id` y `estado_id`
- `usuario-component.ts` - Ahora usa `rol_id`
- `cliente-component.ts` - Ahora usa `ubicacion_local_id`
- `pedido-component.ts` - Ahora usa `estado_id`

---

## 🔄 Estrategia de Serialización

Se ha creado el módulo `serializador.py` en `backend/repositorio/` que contiene funciones para resolver automáticamente las Foreign Keys antes de devolver datos al frontend.

### Uso en Servicios

```python
from repositorio.serializador import serializar_producto

def listar():
    productos = producto_repository.listar()
    # TODO: Obtener categorias y estados del repositorio
    return [serializar_producto(p, categorias, estados_producto) for p in productos]
```

### Funciones Disponibles
- `serializar_producto()` - Resuelve `categoria_id` y `estado_id`
- `serializar_usuario()` - Resuelve `rol_id`
- `serializar_cliente()` - Resuelve `ubicacion_local_id`
- `serializar_proveedor()` - Resuelve `ubicacion_nacional_id`
- `serializar_pedido()` - Resuelve `estado_id`
- `serializar_pedido_detalle()` - Normaliza detalle

---

## 📝 PRÓXIMOS PASOS PARA FINALIZAR LA INTEGRACIÓN

### 1. **Crear Repositorios para Catálogos**
```
✓ categoria_repository.py
✓ estado_producto_repository.py
✓ estado_pedido_repository.py
✓ rol_repository.py
✓ ubicacion_local_repository.py
✓ ubicacion_nacional_repository.py
```

### 2. **Crear Servicios para Catálogos**
```
✓ categoria_service.py
✓ estado_producto_service.py
✓ estado_pedido_service.py
✓ rol_service.py
✓ ubicacion_local_service.py
✓ ubicacion_nacional_service.py
```

### 3. **Actualizar APIs para usar Serializador**
- `producto_api.py` - Usar `serializar_producto()` en GET
- `usuario_api.py` - Usar `serializar_usuario()` en GET
- `cliente_api.py` - Usar `serializar_cliente()` en GET
- `proveedor_api.py` - Usar `serializar_proveedor()` en GET
- `pedido_api.py` - Usar `serializar_pedido()` en GET

### 4. **Actualizar Servicios Backend**
- `producto_service.py` - Integrar con serializador
- `usuario_service.py` - Integrar con serializador
- `cliente_service.py` - Integrar con serializador
- `proveedor_service.py` - Integrar con serializador
- `pedido_service.py` - Integrar con serializador

### 5. **Crear Servicios Angular para Catálogos**
```
✓ categoria.service.ts
✓ estado-producto.service.ts
✓ estado-pedido.service.ts
✓ rol.service.ts
✓ ubicacion-local.service.ts
✓ ubicacion-nacional.service.ts
```

### 6. **Actualizar Componentes HTML**
- Cambiar bindings de `estado` a `estado?.nombre`
- Cambiar bindings de `rol` a `rol?.nombre`
- Cambiar bindings de `telefono/direccion` a `ubicacion?.telefono` y `ubicacion?.direccion`

---

## 🚫 INCOMPATIBILIDADES A EVITAR

❌ **NO usar más `estado` como string** en componentes
```typescript
// MALO:
if (producto.estado === 'ACTIVO') { }

// BIEN:
if (producto.estado?.es_disponible) { }
```

❌ **NO acceder a `telefono` o `direccion` directamente en Cliente/Proveedor**
```typescript
// MALO:
cliente.telefono

// BIEN:
cliente.ubicacion?.telefono
```

❌ **NO usar enum de roles en Usuario**
```typescript
// MALO:
usuario.rol === 'ADMIN'

// BIEN:
usuario.rol?.id === 1  // o comparar por nombre
```

---

## 📊 Diagrama de Relaciones

```
┌─────────────┐
│  Categoria  │ (16 tipos)
└──────┬──────┘
       │ 1:N
       ▼
┌────────────────────────┐
│      Producto         │
└────────────────────────┘
       │ N:1
       ▼
┌──────────────────────┐
│  EstadoProducto      │
└──────────────────────┘

┌──────────────────────┐
│      Rol             │
└──────┬───────────────┘
       │ 1:N
       ▼
┌──────────────────────┐
│      Usuario         │
└──────────────────────┘

┌──────────────────────┐
│  UbicacionLocal      │ (Huancayo)
└──────┬───────────────┘
       │ 1:N
       ▼
┌──────────────────────┐
│      Cliente         │
└──────────────────────┘

┌──────────────────────┐
│ UbicacionNacional    │ (Nacional)
└──────┬───────────────┘
       │ 1:N
       ▼
┌──────────────────────┐
│     Proveedor        │
└──────────────────────┘

┌──────────────────────┐
│  EstadoPedido        │
└──────┬───────────────┘
       │ 1:N
       ▼
┌──────────────────────┐
│       Pedido         │
└──────────────────────┘
```

---

## ✨ Ventajas de la Nueva Estructura

✅ **Sin Redundancias** - Los estados/roles/ubicaciones se definen una sola vez  
✅ **Escalable** - Fácil agregar nuevas categorías, estados, roles, etc.  
✅ **Consistencia** - No hay riesgo de inconsistencias en strings  
✅ **Auditoría** - Se pueden rastrear cambios de estado/rol  
✅ **Reportes** - Mejor agregación y filtrado  
✅ **Normalización 3FN** - Cumple estándares de diseño de bases de datos  

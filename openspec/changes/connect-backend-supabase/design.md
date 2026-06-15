## Context

El proyecto Melius S.A.C tiene un frontend Angular 21 con SSR y un backend FastAPI (Python 3.11+). Actualmente ambos lados almacenan datos en memoria (arreglos en Angular services, listas en Python), sin conexión entre ellos. No hay base de datos, autenticación real, ni endpoints para Proveedores/Compras.

Se busca establecer el flujo completo:

```
┌──────────┐    HTTP (JSON)    ┌──────────┐    SQL     ┌──────────┐
│ Frontend │ ────────────────▶ │ Backend  │ ──────────▶ │ Supabase │
│ (Angular)│ ◀──────────────── │ (FastAPI)│ ◀────────── │ (Postgres│
└──────────┘                   └──────────┘             └──────────┘
     │                              │
  camelCase                     snake_case
  (conversión                    (nativo)
   en cliente HTTP)
```

## Goals / Non-Goals

**Goals:**
- Frontend realiza llamadas HTTP reales al backend para todas las operaciones CRUD
- Backend persiste todos los datos en Supabase (PostgreSQL)
- Backend expone endpoints para: Clientes, Productos, Pedidos, Usuarios, Proveedores, Compras, Dashboard
- Login real: frontend → backend → verifica contra tabla `usuarios` en Supabase → devuelve JWT
- Los JWT incluyen `sub` (user_id), `rol`, `exp` (expiración)
- Endpoints protegidos requieren JWT válido en header `Authorization: Bearer <token>`
- Backend expone API en snake_case; frontend convierte automáticamente

**Non-Goals:**
- Supabase Auth administrado (RLS, magic links) — se usa tabla propia
- SSR (Server-Side Rendering) ya funciona y no se modifica
- Pruebas unitarias/E2E — la prioridad es el flujo funcional
- Despliegue a producción — solo entorno local funcional

## Decisions

| Decisión | Opción Elegida | Alternativas | Razón |
|----------|---------------|--------------|-------|
| Cliente HTTP frontend | `fetch` nativo encapsulado en servicio base | `HttpClient` de Angular, `axios` | Sin dependencia extra, control total de interceptors, liviano. El proyecto ya usa Angular 21 con SSR y `fetch` evita conflictos. |
| ORM / DB client | `supabase` Python library (`supabase-py`) | `psycopg2` directo, SQLAlchemy | Usa la API de Supabase (cliente autenticado), compatible con Row Level Security a futuro. Las queries son SQL directo (`rpc` o `table`). |
| Conversión camelCase ↔ snake_case | `camelcase-keys` / `snakecase-keys` (NPM) + función Python decorator | Manual, interceptors Angular HTTP | Librería ligera y probada. El decorador Python también normaliza automáticamente en los endpoints. |
| JWT | `python-jose` | `PyJWT`, `authlib` | `python-jose` es la recomendada para FastAPI + JWT. Por ahora la password se compara en texto plano. |
| Manejo de errores | Respuesta uniforme: `{"ok": bool, "data": ..., "error": str}` | Excepciones HTTP estándar | Consistente entre frontend y backend, fácil de consumir. |
| ID autoincremental | `SERIAL` en PostgreSQL | UUID | Simplicidad. Los IDs numéricos son más fáciles de depurar y el negocio no requiere escalar a distribución. |

## Data Model (Tablas Supabase)

```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,   -- texto plano (por ahora)
    rol VARCHAR(20) NOT NULL CHECK (rol IN ('ADMIN', 'ALMACENERO', 'VENDEDOR')),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nombres VARCHAR(200) NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL DEFAULT 0,
    estado VARCHAR(20) DEFAULT 'ACTIVO',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id),
    vendedor_id INTEGER REFERENCES usuarios(id),
    estado VARCHAR(20) NOT NULL DEFAULT 'PENDIENTE' CHECK (estado IN ('PENDIENTE', 'ENTREGADO')),
    total DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE pedido_detalles (
    id SERIAL PRIMARY KEY,
    pedido_id INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
    producto_id INTEGER REFERENCES productos(id),
    cantidad INTEGER NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL
);

CREATE TABLE proveedores (
    id SERIAL PRIMARY KEY,
    razon_social VARCHAR(200) NOT NULL,
    ruc VARCHAR(11) UNIQUE NOT NULL,
    telefono VARCHAR(20),
    direccion TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE compras (
    id SERIAL PRIMARY KEY,
    proveedor_id INTEGER REFERENCES proveedores(id),
    total DECIMAL(10,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

## API Contract

Endpoints protegidos requieren header: `Authorization: Bearer <jwt>`

| Método | Endpoint | Auth | Descripción |
|--------|----------|------|-------------|
| POST | `/auth/login` | No | Login, devuelve `{ok, data: {token, usuario}}` |
| GET | `/auth/me` | Sí | Devuelve usuario del token actual |
| GET | `/clientes/` | Sí | Listar clientes |
| POST | `/clientes/` | Sí | Crear cliente |
| PUT | `/clientes/{id}` | Sí | Actualizar cliente |
| DELETE | `/clientes/{id}` | Sí | Eliminar cliente |
| GET | `/productos/` | Sí | Listar productos |
| POST | `/productos/` | Sí | Crear producto |
| PUT | `/productos/{id}` | Sí | Actualizar producto |
| DELETE | `/productos/{id}` | Sí | Eliminar producto |
| GET | `/pedidos/` | Sí | Listar pedidos (con detalles) |
| POST | `/pedidos/` | Sí | Crear pedido (descuenta stock) |
| PUT | `/pedidos/{id}` | Sí | Actualizar pedido |
| DELETE | `/pedidos/{id}` | Sí | Eliminar pedido |
| GET | `/proveedores/` | Sí | Listar proveedores |
| POST | `/proveedores/` | Sí | Crear proveedor |
| PUT | `/proveedores/{id}` | Sí | Actualizar proveedor |
| DELETE | `/proveedores/{id}` | Sí | Eliminar proveedor |
| GET | `/compras/` | Sí | Listar compras |
| POST | `/compras/` | Sí | Crear compra |
| PUT | `/compras/{id}` | Sí | Actualizar compra |
| DELETE | `/compras/{id}` | Sí | Eliminar compra |
| GET | `/usuarios/` | Sí (ADMIN) | Listar usuarios |
| POST | `/usuarios/` | Sí (ADMIN) | Crear usuario |
| PUT | `/usuarios/{id}` | Sí (ADMIN) | Actualizar usuario |
| DELETE | `/usuarios/{id}` | Sí (ADMIN) | Eliminar usuario |
| GET | `/dashboard/resumen` | Sí | Resumen del dashboard |

## Frontend HTTP Layer

```
┌─────────────────────────────────────────────────┐
│                 Angular Service                  │
│  ┌───────────────────────────────────────────┐   │
│  │         BaseHttpService                   │   │
│  │  - get<T>(url) → Promise<T>               │   │
│  │  - post<T>(url, body) → Promise<T>        │   │
│  │  - put<T>(url, body) → Promise<T>         │   │
│  │  - delete<T>(url) → Promise<T>            │   │
│  │  - transformKeys(obj, direction)          │   │
│  │  - maneja errores, token en header        │   │
│  └───────────────────────────────────────────┘   │
│                                                  │
│  ┌──────────┐ ┌───────────┐ ┌────────────────┐   │
│  │ClienteSrv│ │ProductoSrv│ │... (cada entidad)│   │
│  └──────────┘ └───────────┘ └────────────────┘   │
│       │ llama a BaseHttpService                   │
└─────────────────────────────────────────────────┘
```

Cada service de Angular se vuelve un wrapper delgado que llama al `BaseHttpService` con la URL del endpoint correspondiente.

## Risks / Trade-offs

| Riesgo | Mitigación |
|--------|------------|
| [R1] Caída de Supabase bloquea todo el sistema | El backend no debe cachear datos críticos. El frontend muestra error amigable "Servicio no disponible". |
| [R2] Passwords en texto plano | Riesgo conocido y aceptado para MVP. Se migrará a bcrypt en una mejora futura. |
| [R3] Conversión camelCase ↔ snake_case puede omitir campos anidados | El conversor debe ser recursivo. Probar con PedidoDetalle (array anidado). |
| [R4] Bug existente en `pedido_service.py` (firma incorrecta) | Se reescribe completamente el servicio de pedidos; el bug desaparece con la nueva implementación. |
| [R5] JWT sin refresh token | Tiempo de expiración largo (24h) para MVP. A futuro se puede agregar refresh. |

## Migration Plan

1. Configurar proyecto Supabase, crear tablas con SQL anterior
2. Insertar usuarios de prueba con password en texto plano
3. Agregar dependencias Python (`supabase`, `python-jose`, `cryptography`, `python-dotenv`)
4. Crear módulo de configuración (variables de entorno)
5. Reescribir repositorios (usar Supabase client en lugar de listas)
6. Agregar endpoints de `proveedores` y `compras`
7. Implementar auth (login + JWT + middleware)
8. Corregir bug `pedido_service.descontar_stock`
9. Instalar `camelcase-keys` / `snakecase-keys` en frontend
10. Crear `BaseHttpService` en frontend
11. Reescribir todos los servicios Angular para usar HTTP
12. Probar flujo completo

## Open Questions

- ¿Se necesita paginación desde el inicio o basta con listar todo? → A definir durante implementación
- ¿El dashboard debe obtener datos del backend (`/dashboard/resumen`) o calcular localmente con los datos recibidos? → Se implementa endpoint separado como ya existe

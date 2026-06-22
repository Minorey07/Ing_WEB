## Why

El frontend (Angular) y el backend (FastAPI) operan de forma completamente aislada, cada uno con datos en memoria que se pierden al recargar/ reiniciar. No hay persistencia real, la autenticación es ficticia (usuarios hardcodeados en frontend) y el backend carece de endpoints para Proveedores y Compras que el frontend ya consume. Esto hace que el sistema sea inservible para un entorno real.

Se necesita conectar frontend → backend → repositorio → Supabase (base de datos real), unificando el flujo de datos y habilitando autenticación segura con JWT.

## What Changes

- **Frontend**: Todos los servicios (Cliente, Producto, Pedido, Compra, Proveedor, Usuario, Auth) dejan de usar arreglos en memoria y realizan llamadas HTTP al backend. Se crea una capa HTTP centralizada.
- **Backend**: Todos los repositorios migran de listas en Python a consultas SQL contra Supabase (PostgreSQL).
- **Nuevos endpoints**: Se agregan `proveedor_api` y `compra_api` con sus servicios y repositorios.
- **Autenticación real**: Login contra tabla `usuarios` en Supabase, backend genera y valida JWT.
- **Bug corregido**: `pedido_service.descontar_stock` recibe parámetros incorrectos (firma incompatible).
- **Naming**: La API expone snake_case; el frontend transforma camelCase ↔ snake_case en la capa HTTP.
- **Dependencias**: Se agregan `supabase`, `passlib`, `python-jose` (JWT), `bcrypt` al backend.

## Capabilities

### New Capabilities

- `http-client`: Capa HTTP en el frontend que reemplaza los servicios en memoria por llamadas fetch/HttpClient al backend FastAPI. Incluye transformación camelCase ↔ snake_case y manejo de errores centralizado.
- `user-auth-jwt`: Autenticación de usuarios contra tabla `usuarios` en Supabase vía backend. Login devuelve JWT con rol incluido. Middleware de verificación en endpoints protegidos.
- `supabase-persistence`: Repositorios del backend que ejecutan CRUD real contra Supabase (PostgreSQL). Incluye schemas SQL para crear las tablas (clientes, productos, pedidos, pedido_detalles, usuarios, proveedores, compras).

### Modified Capabilities

- *(none)*

## Impact

- `melius-backend/pyproject.toml`: nuevas dependencias
- `melius-backend/`: todos los repositorios reescritos, nuevos APIs (proveedor, compra)
- `Programa_Final_Frontend/src/app/services/`: todos los servicios reescritos para usar HTTP
- `Programa_Final_Frontend/src/app/models/`: se añaden interfaces para DTOs snake_case
- Se necesita un proyecto Supabase activo con las tablas creadas
- Variables de entorno: `SUPABASE_URL`, `SUPABASE_KEY`, `JWT_SECRET`

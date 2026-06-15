## 1. Supabase Setup

- [ ] 1.1 Crear proyecto Supabase en `https://supabase.com` y obtener URL + anon key
- [ ] 1.2 Ejecutar SQL de creación de tablas (usuarios, clientes, productos, pedidos, pedido_detalles, proveedores, compras) desde el SQL Editor de Supabase
- [ ] 1.3 Insertar usuarios de prueba con password en texto plano:
      ```sql
      INSERT INTO usuarios (nombre, correo, password, rol) VALUES
        ('Admin', 'admin@melius.com', '123', 'ADMIN'),
        ('Almacenero', 'almacen@melius.com', '123', 'ALMACENERO'),
        ('Vendedor', 'vendedor@melius.com', '123', 'VENDEDOR');
      ```

## 2. Backend Dependencies & Config

- [x] 2.1 Agregar dependencias a `melius-backend/pyproject.toml`: `supabase`, `python-jose[cryptography]`, `python-dotenv`
- [x] 2.2 Crear `melius-backend/config.py` que lea `SUPABASE_URL`, `SUPABASE_KEY`, `JWT_SECRET`, `JWT_ALGORITHM=HS256` desde variables de entorno o archivo `.env`
- [x] 2.3 Crear `melius-backend/.env` (no committear) con valores de Supabase

## 3. Backend Auth (JWT)

- [x] 3.1 Crear `melius-backend/auth/` con `__init__.py`, `jwt_handler.py` (crear/verificar JWT) y `dependencies.py` (dependencia FastAPI para extraer usuario del token)
- [x] 3.2 Crear `melius-backend/apis/auth_api.py` con endpoints `POST /auth/login` y `GET /auth/me`
- [x] 3.3 Implementar `usuario_service.verificar_login(correo, password)` que consulta Supabase y compara password en texto plano
- [x] 3.4 Registrar `auth_api.router` en `main.py`
- [x] 3.5 Agregar middleware/dependencia `get_current_user` que verifica JWT en endpoints protegidos

## 4. Backend Repositories (Supabase)

- [x] 4.1 Crear `melius-backend/db.py` con inicialización del cliente Supabase (`create_client(SupabaseURL, SupabaseKey)`)
- [x] 4.2 Reescribir `repositorio/cliente_repository.py` para usar Supabase (`tabla: clientes`)
- [x] 4.3 Reescribir `repositorio/producto_repository.py` para usar Supabase (`tabla: productos`)
- [x] 4.4 Reescribir `repositorio/pedido_repository.py` para usar Supabase (tablas: pedidos + pedido_detalles, JOIN)
- [x] 4.5 Reescribir `repositorio/usuario_repository.py` para usar Supabase (`tabla: usuarios`)
- [x] 4.6 Crear `repositorio/proveedor_repository.py` para Supabase (`tabla: proveedores`)
- [x] 4.7 Crear `repositorio/compra_repository.py` para Supabase (`tabla: compras`)

## 5. Backend Services & APIs (completar entidades)

- [x] 5.1 Crear `servicios/proveedor_service.py` con CRUD delegando a proveedor_repository
- [x] 5.2 Crear `servicios/compra_service.py` con CRUD delegando a compra_repository
- [x] 5.3 Crear `apis/proveedor_api.py` con endpoints CRUD protegidos
- [x] 5.4 Crear `apis/compra_api.py` con endpoints CRUD protegidos
- [x] 5.5 Registrar routers en `main.py` (auth, proveedor, compra)
- [x] 5.6 Corregir bug en `pedido_service.py`: reescribir `crear()` para que valide stock en Supabase antes de insertar, y `descontar_stock` reciba `producto_id` y `cantidad`
- [x] 5.7 Actualizar `dashboard_service.py` para consultar Supabase directamente
- [x] 5.8 Actualizar `apis/dashboard_api.py` para usar dependencia JWT
- [x] 5.9 Actualizar `apis/cliente_api.py`, `producto_api.py`, `pedido_api.py`, `usuario_api.py` para inyectar `get_current_user` y usar response uniforme `{ok, data, error}`

## 6. Frontend Dependencies

- [x] 6.1 Instalar `camelcase-keys` y `snakecase-keys` en frontend: `npm install camelcase-keys snakecase-keys`

## 7. Frontend Base HTTP Layer

- [x] 7.1 Crear `src/app/services/base-http.service.ts` con métodos genéricos `get`, `post`, `put`, `delete` usando `fetch`
- [x] 7.2 Implementar transformación recursiva camelCase ↔ snake_case en base-http.service
- [x] 7.3 Implementar inyección automática de JWT desde localStorage en base-http.service
- [x] 7.4 Implementar manejo de errores centralizado (parsear respuesta `{ok, data, error}`)

## 8. Frontend Services (migrar a HTTP)

- [x] 8.1 Reescribir `auth.service.ts`: login via `POST /auth/login`, guardar JWT en localStorage, método `getToken()`, `logout()` limpia token
- [x] 8.2 Reescribir `cliente.service.ts`: usar BaseHttpService para CRUD contra `/clientes/`
- [x] 8.3 Reescribir `producto.service.ts`: usar BaseHttpService para CRUD contra `/productos/`
- [x] 8.4 Reescribir `pedido.service.ts`: usar BaseHttpService para CRUD contra `/pedidos/`
- [x] 8.5 Reescribir `compra.service.ts`: usar BaseHttpService para CRUD contra `/compras/`
- [x] 8.6 Reescribir `proveedor.service.ts`: usar BaseHttpService para CRUD contra `/proveedores/`
- [x] 8.7 Reescribir `usuario.service.ts`: usar BaseHttpService para CRUD contra `/usuarios/`

## 9. Frontend Guards & Components

- [x] 9.1 Actualizar `auth.guard.ts`: verificar existencia de JWT en localStorage (AuthService.isLoggedIn chequea token) — sin cambios necesarios, ya funciona con isLoggedIn()
- [x] 9.2 Actualizar `dashboard-home.ts`: obtener datos de `GET /dashboard/resumen` y pasar de promesa a señal
- [x] 9.3 Verificar que todos los componentes funcionan con servicios asíncronos (cambiar señales/listas sincrónicas a Promesas/async)

## 10. Integration & Testing

- [ ] 10.1 Iniciar backend: `uvicorn main:app --reload` y verificar que conecta con Supabase
- [ ] 10.2 Iniciar frontend: `npm start` y verificar login real contra backend
- [ ] 10.3 Probar CRUD completo de Clientes, Productos, Pedidos, Proveedores, Compras, Usuarios
- [ ] 10.4 Verificar que pedidos descuentan stock en Supabase
- [ ] 10.5 Verificar que dashboard muestra datos reales desde backend
- [ ] 10.6 Verificar que roles funcionan (admin ve usuarios, almacenero no)
- [ ] 10.7 Probar manejo de errores: token inválido, stock insuficiente, credenciales incorrectas

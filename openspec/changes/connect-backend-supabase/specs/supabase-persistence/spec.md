## ADDED Requirements

### Requirement: Backend uses Supabase as database
All backend repositories SHALL use the Supabase Python client to perform CRUD operations instead of in-memory lists.

#### Scenario: Repository initialization
- **WHEN** the application starts
- **THEN** each repository SHALL be initialized with a Supabase client using `SUPABASE_URL` and `SUPABASE_KEY` from environment variables

#### Scenario: Read from Supabase table
- **WHEN** `repository.listar()` is called
- **THEN** the repository SHALL execute a `SELECT * FROM <table>` query via the Supabase client and return the results

#### Scenario: Create row in Supabase table
- **WHEN** `repository.crear(entity)` is called
- **THEN** the repository SHALL execute an `INSERT INTO <table>` query and return the created row with its generated ID

#### Scenario: Update row in Supabase table
- **WHEN** `repository.actualizar(entity)` is called
- **THEN** the repository SHALL execute an `UPDATE <table> SET ... WHERE id = <id>` query

#### Scenario: Delete row from Supabase table
- **WHEN** `repository.eliminar(id)` is called
- **THEN** the repository SHALL execute a `DELETE FROM <table> WHERE id = <id>` query

### Requirement: Cliente repository persisted
The `cliente_repository` SHALL operate on the `clientes` table in Supabase.

#### Scenario: Full CRUD cycle
- **WHEN** a cliente is created, listed, updated, and deleted
- **THEN** all operations SHALL reflect immediately in the Supabase `clientes` table

### Requirement: Producto repository persisted
The `producto_repository` SHALL operate on the `productos` table in Supabase, including stock management.

#### Scenario: Stock deduction on pedido creation
- **WHEN** a pedido is created
- **THEN** the `producto_service.descontar_stock()` SHALL update `productos.stock` in Supabase by subtracting each detalle.cantidad

#### Scenario: Stock validation before deduction
- **WHEN** creating a pedido with a detalle where cantidad > producto.stock
- **THEN** the service SHALL reject the operation with HTTP 400 `{ok: false, error: "Stock insuficiente para producto X"}`

### Requirement: Pedido repository persisted with detalles
The `pedido_repository` SHALL operate on the `pedidos` and `pedido_detalles` tables in Supabase.

#### Scenario: Create pedido with detalles
- **WHEN** a pedido is created
- **THEN** the repository SHALL insert one row in `pedidos` and one row per detalle in `pedido_detalles` with the generated pedido_id

#### Scenario: List pedidos with detalles
- **WHEN** `pedido_repository.listar()` is called
- **THEN** the repository SHALL fetch pedidos JOINed with their detalles and return the full structure

#### Scenario: Delete pedido cascades to detalles
- **WHEN** a pedido is deleted
- **THEN** the repository SHALL delete from `pedido_detalles` WHERE pedido_id = <id> AND then delete from `pedidos` WHERE id = <id>

### Requirement: Usuario repository persisted
The `usuario_repository` SHALL operate on the `usuarios` table in Supabase.

#### Scenario: Create user with plain text password
- **WHEN** a new user is created
- **THEN** the password SHALL be stored in plain text (MVP only, no hashing)

### Requirement: Proveedor repository (new)
The `proveedor_repository` SHALL be created to operate on the `proveedores` table in Supabase.

#### Scenario: Full CRUD cycle
- **WHEN** a proveedor is created, listed, updated, and deleted
- **THEN** all operations SHALL work against the `proveedores` table

### Requirement: Compra repository (new)
The `compra_repository` SHALL be created to operate on the `compras` table in Supabase.

#### Scenario: Full CRUD cycle
- **WHEN** a compra is created, listed, updated, and deleted
- **THEN** all operations SHALL work against the `compras` table

### Requirement: New API endpoints for Proveedores
The backend SHALL expose a `proveedores` router with full CRUD endpoints.

#### Scenario: CRUD routes exist
- **WHEN** the backend starts
- **THEN** `GET /proveedores/`, `POST /proveedores/`, `PUT /proveedores/{id}`, `DELETE /proveedores/{id}` SHALL be available and protected by JWT

### Requirement: New API endpoints for Compras
The backend SHALL expose a `compras` router with full CRUD endpoints.

#### Scenario: CRUD routes exist
- **WHEN** the backend starts
- **THEN** `GET /compras/`, `POST /compras/`, `PUT /compras/{id}`, `DELETE /compras/{id}` SHALL be available and protected by JWT

### Requirement: Dashboard service uses Supabase
The `dashboard_service` SHALL compute its summary by querying Supabase tables.

#### Scenario: Summary query
- **WHEN** `dashboard_service.resumen()` is called
- **THEN** it SHALL return `{total_ventas, pendientes, entregados, productos_stock}` computed from `pedidos` and `productos` tables

### Requirement: Environment configuration
The backend SHALL read Supabase credentials and JWT secret from environment variables.

#### Scenario: Environment variables loaded
- **WHEN** the backend starts
- **THEN** it SHALL read `SUPABASE_URL`, `SUPABASE_KEY`, and `JWT_SECRET` from environment variables or a `.env` file and fail with a clear error if any are missing

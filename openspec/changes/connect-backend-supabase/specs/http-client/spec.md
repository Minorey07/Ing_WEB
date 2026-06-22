## ADDED Requirements

### Requirement: HTTP client base service
The system SHALL provide a base Angular injectable service (`BaseHttpService`) that encapsulates all HTTP communication with the backend API.

#### Scenario: GET request with JWT token
- **WHEN** any service calls `BaseHttpService.get<T>(url)`
- **THEN** the request SHALL include `Authorization: Bearer <token>` header (if token exists in localStorage) AND the response SHALL be deserialized from snake_case to camelCase keys recursively

#### Scenario: POST request with body
- **WHEN** any service calls `BaseHttpService.post<T>(url, body)`
- **THEN** the request body SHALL be serialized from camelCase to snake_case keys recursively AND the response SHALL be deserialized back to camelCase

#### Scenario: PUT request with body
- **WHEN** any service calls `BaseHttpService.put<T>(url, body)`
- **THEN** the behavior SHALL match POST serialization/deserialization rules

#### Scenario: DELETE request
- **WHEN** any service calls `BaseHttpService.delete<T>(url)`
- **THEN** a DELETE request SHALL be sent with the JWT token in the Authorization header

#### Scenario: Error handling
- **WHEN** the backend returns a non-2xx status code
- **THEN** the `BaseHttpService` SHALL parse the `{ok: false, error: string}` response and throw an Error with the error message

#### Scenario: No token available
- **WHEN** a request is made and no JWT token exists in localStorage
- **THEN** the request SHALL be sent without Authorization header

### Requirement: Cliente service HTTP
The frontend `ClienteService` SHALL perform CRUD operations via HTTP to the backend instead of in-memory arrays.

#### Scenario: Listar clientes
- **WHEN** `ClienteService.listar()` is called
- **THEN** it SHALL call `GET /clientes/` via BaseHttpService and return the deserialized array of clientes

#### Scenario: Crear cliente
- **WHEN** `ClienteService.crear(cliente)` is called
- **THEN** it SHALL call `POST /clientes/` with the serialized body and return the created cliente

#### Scenario: Actualizar cliente
- **WHEN** `ClienteService.actualizar(cliente)` is called
- **THEN** it SHALL call `PUT /clientes/{id}` with the serialized body

#### Scenario: Eliminar cliente
- **WHEN** `ClienteService.eliminar(id)` is called
- **THEN** it SHALL call `DELETE /clientes/{id}`

### Requirement: Producto service HTTP
The frontend `ProductoService` SHALL perform CRUD operations via HTTP.

#### Scenario: Listar productos
- **WHEN** `ProductoService.listar()` is called
- **THEN** it SHALL call `GET /productos/` via BaseHttpService

#### Scenario: Crear producto
- **WHEN** `ProductoService.crear(producto)` is called
- **THEN** it SHALL call `POST /productos/` with the serialized body

#### Scenario: Actualizar producto
- **WHEN** `ProductoService.actualizar(producto)` is called
- **THEN** it SHALL call `PUT /productos/{id}` with the serialized body

#### Scenario: Eliminar producto
- **WHEN** `ProductoService.eliminar(id)` is called
- **THEN** it SHALL call `DELETE /productos/{id}`

#### Scenario: Descontar stock via pedido
- **WHEN** a pedido is created with detalles
- **THEN** stock validation and deduction SHALL happen on the backend, not in the frontend

### Requirement: Pedido service HTTP
The frontend `PedidoService` SHALL perform CRUD operations via HTTP.

#### Scenario: Listar pedidos
- **WHEN** `PedidoService.listar()` is called
- **THEN** it SHALL call `GET /pedidos/` via BaseHttpService and return pedidos with their detalles

#### Scenario: Crear pedido
- **WHEN** `PedidoService.crear(pedido)` is called
- **THEN** it SHALL call `POST /pedidos/` with the serialized body (including detalles array)

#### Scenario: Actualizar pedido
- **WHEN** `PedidoService.actualizar(pedido)` is called
- **THEN** it SHALL call `PUT /pedidos/{id}` with the serialized body

#### Scenario: Eliminar pedido
- **WHEN** `PedidoService.eliminar(id)` is called
- **THEN** it SHALL call `DELETE /pedidos/{id}`

### Requirement: Compra service HTTP
The frontend `CompraService` SHALL perform CRUD operations via HTTP.

#### Scenario: Listar compras
- **WHEN** `CompraService.listar()` is called
- **THEN** it SHALL call `GET /compras/` via BaseHttpService

#### Scenario: Crear compra
- **WHEN** `CompraService.crear(compra)` is called
- **THEN** it SHALL call `POST /compras/` with the serialized body

#### Scenario: Actualizar compra
- **WHEN** `CompraService.actualizar(compra)` is called
- **THEN** it SHALL call `PUT /compras/{id}` with the serialized body

#### Scenario: Eliminar compra
- **WHEN** `CompraService.eliminar(id)` is called
- **THEN** it SHALL call `DELETE /compras/{id}`

### Requirement: Proveedor service HTTP
The frontend `ProveedorService` SHALL perform CRUD operations via HTTP.

#### Scenario: Listar proveedores
- **WHEN** `ProveedorService.listar()` is called
- **THEN** it SHALL call `GET /proveedores/` via BaseHttpService

#### Scenario: Crear proveedor
- **WHEN** `ProveedorService.crear(proveedor)` is called
- **THEN** it SHALL call `POST /proveedores/` with the serialized body

#### Scenario: Actualizar proveedor
- **WHEN** `ProveedorService.actualizar(proveedor)` is called
- **THEN** it SHALL call `PUT /proveedores/{id}` with the serialized body

#### Scenario: Eliminar proveedor
- **WHEN** `ProveedorService.eliminar(id)` is called
- **THEN** it SHALL call `DELETE /proveedores/{id}`

### Requirement: Usuario service HTTP (admin only)
The frontend `UsuarioService` SHALL perform CRUD operations via HTTP for admin user management.

#### Scenario: Listar usuarios
- **WHEN** `UsuarioService.listar()` is called
- **THEN** it SHALL call `GET /usuarios/` via BaseHttpService

#### Scenario: Crear usuario
- **WHEN** `UsuarioService.crear(usuario)` is called
- **THEN** it SHALL call `POST /usuarios/` with the serialized body

#### Scenario: Actualizar usuario
- **WHEN** `UsuarioService.actualizar(usuario)` is called
- **THEN** it SHALL call `PUT /usuarios/{id}` with the serialized body

#### Scenario: Eliminar usuario
- **WHEN** `UsuarioService.eliminar(id)` is called
- **THEN** it SHALL call `DELETE /usuarios/{id}`

### Requirement: Frontend models SHALL include snake_case DTO interfaces
The frontend SHALL define DTO interfaces matching the backend snake_case JSON shape for serialization/deserialization.

#### Scenario: Mapping exists for all entities
- **WHEN** a request is serialized or response deserialized
- **THEN** the BaseHttpService SHALL recursively transform keys between camelCase (internal) and snake_case (wire format)

### Requirement: Dashboard service fetches data from backend
The `DashboardHome` component SHALL fetch dashboard data from `GET /dashboard/resumen` via HTTP.

#### Scenario: Load dashboard summary
- **WHEN** `DashboardHome` initializes
- **THEN** it SHALL call `GET /dashboard/resumen` and display total_ventas, pendientes, entregados, productos_stock

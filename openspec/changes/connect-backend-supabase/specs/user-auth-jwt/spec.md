## ADDED Requirements

### Requirement: Login against backend API
The frontend `AuthService` SHALL authenticate users by sending credentials to the backend instead of checking a hardcoded list.

#### Scenario: Successful login
- **WHEN** user submits correo and password via `AuthService.login(correo, password)`
- **THEN** the service SHALL call `POST /auth/login` with `{correo, password}` and on success SHALL store the returned JWT token in localStorage

#### Scenario: Failed login
- **WHEN** user submits invalid credentials
- **THEN** the backend SHALL return `{ok: false, error: "Credenciales inválidas"}` and the frontend SHALL display the error message

### Requirement: Backend login endpoint with JWT
The backend SHALL provide a `POST /auth/login` endpoint that validates credentials against the `usuarios` table in Supabase and returns a JWT.

#### Scenario: Valid credentials
- **WHEN** `POST /auth/login` receives `{correo, password}`
- **THEN** the backend SHALL query `usuarios` by correo, compare password in plain text, and if valid SHALL return `{ok: true, data: {token: <jwt>, usuario: {id, nombre, correo, rol}}}`

#### Scenario: Invalid credentials
- **WHEN** `POST /auth/login` receives incorrect password or non-existent correo
- **THEN** the backend SHALL return `{ok: false, error: "Credenciales inválidas"}` with HTTP 401

#### Scenario: Password stored in plain text
- **WHEN** a new user is created via `POST /usuarios/`
- **THEN** the backend SHALL store the password as-is in the `usuarios` table (plain text, MVP only)

### Requirement: JWT token structure
The JWT token SHALL contain the user ID and role for authorization.

#### Scenario: Token payload
- **WHEN** a JWT is generated on login
- **THEN** the token SHALL contain `sub` (user id), `rol` (user role), and `exp` (expiration timestamp)

#### Scenario: Token verification middleware
- **WHEN** a request arrives at a protected endpoint
- **THEN** the backend SHALL verify the JWT from the `Authorization: Bearer <token>` header, reject with HTTP 401 if invalid or expired, and attach the decoded user info to the request context

### Requirement: Backend auth middleware
The backend SHALL have a reusable dependency/ middleware to protect endpoints with JWT verification.

#### Scenario: Protected endpoint with valid token
- **WHEN** a request with a valid JWT hits a protected endpoint
- **THEN** the middleware SHALL allow the request and inject `current_user` into the route handler

#### Scenario: Protected endpoint without token
- **WHEN** a request without Authorization header hits a protected endpoint
- **THEN** the middleware SHALL return HTTP 401 `{ok: false, error: "Token requerido"}`

#### Scenario: Protected endpoint with expired token
- **WHEN** a request with an expired JWT hits a protected endpoint
- **THEN** the middleware SHALL return HTTP 401 `{ok: false, error: "Token expirado"}`

#### Scenario: Admin-only endpoint
- **WHEN** a non-ADMIN user requests `GET /usuarios/`
- **THEN** the backend SHALL return HTTP 403 `{ok: false, error: "No autorizado"}`

### Requirement: AuthGuard uses JWT presence
The frontend `AuthGuard` SHALL check for a JWT in localStorage to determine if the user is logged in.

#### Scenario: JWT exists
- **WHEN** a JWT token exists in localStorage
- **THEN** the `authGuard` SHALL allow navigation

#### Scenario: No JWT
- **WHEN** no JWT token exists
- **THEN** the `authGuard` SHALL redirect to `/login`

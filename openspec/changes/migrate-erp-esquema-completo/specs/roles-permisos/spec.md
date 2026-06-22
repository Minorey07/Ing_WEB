## ADDED Requirements

### Requirement: Tabla roles con datos semilla
El sistema SHALL tener una tabla `roles` con los roles del sistema, y `usuarios` SHALL referenciar `roles` mediante `rol_id`.

#### Scenario: Tabla roles creada
- **WHEN** se ejecuta la migración Fase 1
- **THEN** la tabla `roles` SHALL existir con `id` (PK) y `nombre` (TEXT UNIQUE)
- **AND** SHALL contener: `(1, 'ADMIN')`, `(2, 'ALMACENERO')`, `(3, 'VENDEDOR')`

#### Scenario: usuarios.rol_id migrado
- **WHEN** se ejecuta la migración
- **THEN** `usuarios.rol` (TEXT) SHALL ser reemplazado por `usuarios.rol_id` (BIGINT FK → roles.id)
- **AND** `usuarios.rol_id` SHALL ser NOT NULL

### Requirement: Backend valida permisos por rol_id
Los endpoints SHALL usar el `rol_id` del usuario autenticado (extraído del JWT) para validar permisos, no el nombre del rol como texto.

#### Scenario: JWT contiene rol_id
- **WHEN** un usuario inicia sesión
- **THEN** el token JWT SHALL incluir `rol_id` (int) además de `rol` (string) para retrocompatibilidad

#### Scenario: require_roles usa rol_id
- **WHEN** un endpoint protegido por `require_roles` es accedido
- **THEN** la validación SHALL usar `rol_id` para determinar pertenencia al rol

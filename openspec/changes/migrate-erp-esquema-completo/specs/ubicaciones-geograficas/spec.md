## ADDED Requirements

### Requirement: Tablas de ubicaciones
El sistema SHALL tener dos tablas de ubicaciones: `ubicaciones_locales` (para clientes) y `ubicaciones_nacionales` (para proveedores).

#### Scenario: Tablas de ubicaciones creadas
- **WHEN** se ejecuta la migración Fase 3
- **THEN** `ubicaciones_locales` SHALL existir con `id` (PK), `nombre` (TEXT), `distrito` (TEXT), `provincia` (TEXT), `departamento` (TEXT)
- **AND** `ubicaciones_nacionales` SHALL existir con `id` (PK), `nombre` (TEXT), `region` (TEXT), `pais` (TEXT)

### Requirement: clientes con FK a ubicacion_local_id
La tabla `clientes` SHALL incluir `ubicacion_local_id` como FK opcional.

#### Scenario: Columna ubicacion_local_id en clientes
- **WHEN** se ejecuta la migración Fase 3
- **THEN** `clientes.ubicacion_local_id` (BIGINT FK → ubicaciones_locales.id) SHALL existir
- **AND** SHALL ser nullable

### Requirement: proveedores con FK a ubicacion_nacional_id
La tabla `proveedores` SHALL incluir `ubicacion_nacional_id` como FK opcional.

#### Scenario: Columna ubicacion_nacional_id en proveedores
- **WHEN** se ejecuta la migración Fase 3
- **THEN** `proveedores.ubicacion_nacional_id` (BIGINT FK → ubicaciones_nacionales.id) SHALL existir
- **AND** SHALL ser nullable

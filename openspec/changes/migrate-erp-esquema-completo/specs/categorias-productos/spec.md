## ADDED Requirements

### Requirement: Tabla categorias
El sistema SHALL tener una tabla `categorias` para clasificar productos.

#### Scenario: Tabla categorias creada
- **WHEN** se ejecuta la migración Fase 2
- **THEN** la tabla `categorias` SHALL existir con `id` (PK), `nombre` (TEXT UNIQUE), `descripcion` (TEXT)

### Requirement: Producto tiene categoria_id
La tabla `productos` SHALL incluir `categoria_id` como FK opcional a `categorias`.

#### Scenario: Columna categoria_id en productos
- **WHEN** se ejecuta la migración Fase 2
- **THEN** `productos.categoria_id` (BIGINT FK → categorias.id) SHALL existir
- **AND** SHALL ser nullable (un producto puede no tener categoría)

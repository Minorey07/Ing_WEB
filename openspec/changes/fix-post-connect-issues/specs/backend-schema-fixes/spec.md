## ADDED Requirements

### Requirement: Producto schema includes estado field
The backend `Producto` schema SHALL include an `estado` field matching the existing Supabase column.

#### Scenario: Producto returned with estado
- **WHEN** the backend returns a producto from any endpoint
- **THEN** the response SHALL include `estado` with value `"ACTIVO"` or `"AGOTADO"`

#### Scenario: Producto created by frontend includes estado
- **WHEN** the frontend sends a producto with `estado` field
- **THEN** the backend SHALL accept and store it via Supabase

### Requirement: Python packages have __init__.py
All backend Python packages SHALL have `__init__.py` files for explicit package declaration.

#### Scenario: Packages importable
- **WHEN** Python imports `apis`, `repositorio`, `servicios`, or `esquema`
- **THEN** the import SHALL succeed without errors

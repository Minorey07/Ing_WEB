## Context

El cambio `connect-backend-supabase` implementó la conexión frontend → backend → Supabase, pero durante la revisión pre-testing se detectaron issues que impedirían el funcionamiento correcto:

1. **Schema Producto incompleto**: El backend no tiene el campo `estado`, el frontend lo necesita para mostrar estado ACTIVO/AGOTADO
2. **Faltan `__init__.py`**: Los packages Python `apis/`, `repositorio/`, `servicios/`, `esquema/` no tienen `__init__.py`, lo que puede causar errores de importación dependiendo de cómo se ejecute `uvicorn`

## Goals / Non-Goals

**Goals:**
- Agregar `estado: str` al schema `Producto` del backend
- Actualizar `producto_repository` para manejar `estado`
- Crear `__init__.py` en los 4 packages Python

**Non-Goals:**
- No se modifican tablas de Supabase (la columna `estado` ya existe)
- No se modifican endpoints ni lógica de negocio
- No se toca el frontend

## Decisions

| Decisión | Opción | Razón |
|----------|--------|-------|
| Valor default de `estado` | `"ACTIVO"` | Coincide con el default en la tabla SQL de Supabase |
| `__init__.py` vacíos | Archivos sin contenido | Suficiente para marcar el directorio como package Python |

## Risks / Trade-offs

- [R1] Que `producto_repository.actualizar()` no incluya `estado` en el update → Se corrige explícitamente en el cambio
- [R2] Que Pydantic v2 ignore `estado` si no se agrega al schema → Es el bug que estamos corrigiendo

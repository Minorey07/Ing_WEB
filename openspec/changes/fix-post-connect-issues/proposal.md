## Why

La implementación de la conexión backend-Supabase dejó issues detectados en la revisión previa a testing: el schema backend de Producto no incluye el campo `estado` que el frontend usa, faltan `__init__.py` en los packages Python, y hay detalles menores de robustez. Si no se corrigen ahora, el frontend perderá datos y pueden ocurrir errores de importación.

## What Changes

- **Backend `esquema/producto.py`**: Agregar campo `estado: str` al schema Producto para que el backend retorne el estado que el frontend espera
- **Backend `__init__.py`**: Crear archivos `__init__.py` en `apis/`, `repositorio/`, `servicios/`, `esquema/` para imports explícitos
- **Backend `producto_repository.py`**: Actualizar `actualizar()` para incluir `estado` en los datos enviados a Supabase
- No hay cambios en frontend ni en base de datos

## Capabilities

### New Capabilities
- `backend-schema-fixes`: Correcciones al schema Producto y estructura de packages Python para evitar errores en runtime

### Modified Capabilities
- *(ninguna)*

## Impact

- `melius-backend/esquema/producto.py`: +1 campo (`estado`)
- `melius-backend/apis/__init__.py`: nuevo archivo
- `melius-backend/repositorio/__init__.py`: nuevo archivo
- `melius-backend/servicios/__init__.py`: nuevo archivo
- `melius-backend/esquema/__init__.py`: nuevo archivo

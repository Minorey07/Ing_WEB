## Why

Los gráficos de Chart.js en el dashboard-home no se renderizan aunque los datos numéricos (tarjetas) sí se muestran correctamente. El problema ocurre porque Chart.js intenta crearse múltiples veces sobre el mismo canvas (ngAfterViewInit + cargarDatos) y el canvas condicional por *ngIf puede no existir aún cuando se ejecuta la creación del chart. Esto deja el dashboard sin visualizaciones, afectando a los 3 roles (ADMIN, ALMACENERO, VENDEDOR).

## What Changes

- `dashboard-home.ts`: Reemplazar el uso de `document.getElementById` + `new Chart()` por un patrón que:
  - Use `Chart.getChart()` para detectar y destruir charts existentes antes de crear nuevos
  - Elimine la doble creación (ngAfterViewInit vs cargarDatos)
  - Garantice que el canvas exista antes de crear el chart
- `dashboard-home.html`: Actualizar identificadores de canvas para usar ViewChild en lugar de IDs planas (o mantener IDs pero con prefijo único por rol)

No hay cambios en backend, Supabase, rutas, guards, servicios ni estructura del proyecto.

## Capabilities

### New Capabilities
- `chart-rendering`: Manejo correcto del ciclo de vida de Chart.js en Angular con componentes condicionales (*ngIf). Incluye destrucción de charts previos, verificación de existencia del canvas y sincronización con el cambio de señales.

### Modified Capabilities
- (ninguna — no hay cambios en requerimientos de specs existentes)

## Impact

- **Archivos modificados**: `dashboard-home.ts`, `dashboard-home.html`
- **Dependencias**: Chart.js ^4.5.1 (ya instalado, no se agregan nuevas)
- **Riesgo bajo**: Los cambios son puramente de frontend y están aislados en un solo componente

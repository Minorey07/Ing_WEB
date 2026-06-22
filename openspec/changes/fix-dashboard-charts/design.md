## Context

Dashboard-home usa Chart.js v4.5.1 para 3 gráficos (pedidos, stock, ventas) que se renderizan condicionalmente según el rol del usuario mediante `*ngIf`. Actualmente los gráficos no se visualizan por 2 problemas concurrentes:

1. **Doble creación**: `ngAfterViewInit` crea charts con datos vacíos (setTimeout 100ms), y luego `cargarDatos` vuelve a intentarlo sobre el mismo canvas tras la respuesta HTTP. Chart.js v4 lanza error "Canvas is already in use" y el segundo intento falla.
2. **Sin limpieza de instancias**: No hay `chart.destroy()` entre creaciones sucesivas.

## Goals / Non-Goals

**Goals:**
- Los 3 gráficos (pedidos, stock, ventas) se renderizan correctamente para ADMIN
- Los 2 gráficos (pedidos, stock) se renderizan correctamente para ALMACENERO
- El 1 gráfico (pedidos) se renderiza correctamente para VENDEDOR
- Los charts solo se crean después de que los datos de la API están disponibles
- Los charts se destruyen antes de recrearse (soporte para futuras recargas de datos)

**Non-Goals:**
- No se agregan nuevas dependencias
- No se modifica backend, Supabase, rutas, guards ni servicios
- No se cambia la estructura del proyecto
- No se migra a ng2-charts

## Decisions

### Decision 1: Eliminar `ngAfterViewInit` como origen de charts

Se elimina la creación de charts desde `ngAfterViewInit`. Los charts solo se crearán desde `cargarDatos()` después de que los datos de la API hayan cargado.

**Alternativa considerada**: Mantener `ngAfterViewInit` con datos mockeados. Descartado porque confunde al usuario (charts sin datos visibles antes de la carga real).

### Decision 2: Usar `Chart.getChart()` + `destroy()` en lugar de trackear instancias manualmente

Cada función de gráfico (`graficoPedidos`, `graficoStock`, `graficoVentas`) verificará si existe una instancia previa de Chart.js en el canvas usando `Chart.getChart(canvasId)`. Si existe, la destruirá antes de crear una nueva.

**Alternativa considerada**: Mantener un array `Chart[]` privado. Descartado porque `Chart.getChart()` es la API nativa de Chart.js para este propósito y evita estado adicional en el componente.

### Decision 3: No usar ViewChild — mantener `document.getElementById`

Los canvases están dentro de `*ngIf` condicionales, lo que hace que ViewChild no sea fiable (retorna undefined cuando el bloque está oculto). `document.getElementById` con verificación de null previa es más directo y robusto para este caso.

**Alternativa considerada**: ViewChild con `{ static: false }`. Descartado porque el canvas puede no existir al iniciar el componente (depende del rol).

### Decision 4: Patrón defensivo en cada función de gráfico

```typescript
graficoPedidos() {
    const canvas = document.getElementById('chartPedidos');
    if (!canvas) return;
    const chart = Chart.getChart('chartPedidos');
    if (chart) chart.destroy();
    new Chart('chartPedidos', { ... });
}
```

Este patrón:
- Verifica que el canvas exista (por *ngIf condicional)
- Destruye instancias previas (por doble llamado a cargarDatos)
- Crea el chart con datos reales (porque se llama después de la carga de API)

## Risks / Trade-offs

| Riesgo | Mitigación |
|---|---|
| `Chart.getChart()` retorna undefined si no hay chart previo | El código verifica `if (chart)` antes de llamar a `destroy()`, es seguro |
| Si `cargarDatos()` se llama múltiples veces, los charts se recrean | Es el comportamiento deseado para recarga de datos |
| Las IDs de canvas se repiten entre ADMIN/ALMACENERO/VENDEDOR pero solo un bloque *ngIf está activo a la vez | Las IDs pueden coincidir porque solo un conjunto de canvases existe en el DOM en un momento dado |

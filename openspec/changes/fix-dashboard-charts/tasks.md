## 1. Corregir creación de gráficos en dashboard-home.ts

- [x] 1.1 Eliminar `AfterViewInit` y el método `ngAfterViewInit` — los charts solo se crearán desde `cargarDatos` después de la carga de datos
- [x] 1.2 Agregar verificación con `Chart.getChart()` + `destroy()` en `graficoPedidos()`, `graficoStock()` y `graficoVentas()` antes de cada `new Chart()`
- [x] 1.3 Verificar que el canvas existe (`document.getElementById()`) al inicio de cada función de gráfico, retornando si es null

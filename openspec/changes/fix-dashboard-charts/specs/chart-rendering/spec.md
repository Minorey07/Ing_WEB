## ADDED Requirements

### Requirement: Destroy chart before recreating on same canvas
The system SHALL destroy any existing Chart.js instance on a canvas before creating a new chart on that same canvas.

#### Scenario: Chart recreated after data refresh
- **WHEN** `cargarDatos()` completes and calls `recrearGraficos()`
- **THEN** any previous Chart instance on the canvas SHALL be destroyed via `Chart.getChart(canvasId).destroy()` before `new Chart()` is called

#### Scenario: ngAfterViewInit does not create charts
- **WHEN** `ngAfterViewInit` lifecycle hook fires
- **THEN** the system SHALL NOT attempt to create any Chart.js instances

### Requirement: Canvas existence verified before chart creation
The system SHALL verify that the target canvas element exists in the DOM before attempting to create a chart on it.

#### Scenario: Canvas not yet rendered
- **WHEN** `graficoPedidos()`, `graficoStock()`, or `graficoVentas()` is called
- **THEN** the function SHALL check `document.getElementById()` and return immediately if the canvas is null

#### Scenario: Canvas rendered inside *ngIf condition
- **WHEN** the user role is ADMIN and the ADMIN `<ng-container>` is rendered
- **THEN** `chartPedidos`, `chartStock`, and `chartVentas` canvases SHALL exist and charts SHALL be created

#### Scenario: Canvas rendered for ALMACENERO role
- **WHEN** the user role is ALMACENERO
- **THEN** `chartPedidos` and `chartStock` canvases SHALL exist and charts SHALL be created; `chartVentas` canvas SHALL NOT exist

#### Scenario: Canvas rendered for VENDEDOR role
- **WHEN** the user role is VENDEDOR
- **THEN** `chartPedidos` canvas SHALL exist and chart SHALL be created; `chartStock` and `chartVentas` canvases SHALL NOT exist

### Requirement: Chart creation deferred until data is available
The system SHALL create Chart.js instances only after all required data has been loaded from the API.

#### Scenario: Charts created after API response
- **WHEN** `cargarDatos()` finishes fetching products and orders
- **THEN** chart data SHALL reflect the loaded values (pedidosPendientes, pedidosEntregados, productos, totalVentas)
- **AND** charts SHALL NOT be created with zero/empty data before the API responds

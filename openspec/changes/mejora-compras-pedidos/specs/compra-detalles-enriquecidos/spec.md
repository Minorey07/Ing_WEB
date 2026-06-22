## ADDED Requirements

### Requirement: Listar compra_detalles con nombre de producto
El sistema DEBE devolver el nombre del producto (`producto_nombre`) en el listado de compra_detalles, obtenido mediante JOIN con la tabla `productos`.

#### Scenario: Listado incluye nombre del producto
- **WHEN** se invoca `GET /compra-detalles/`
- **THEN** cada detalle en la respuesta incluye `producto_nombre: string` además de `producto_id: number`

### Requirement: Auto-incremento de stock al registrar compra_detalle
El sistema DEBE incrementar `productos.stock` automáticamente en la cantidad comprada cuando se crea un nuevo `compra_detalle`.

#### Scenario: Stock se incrementa al crear detalle
- **WHEN** se invoca `POST /compra-detalles/` con `producto_id: 5` y `cantidad: 10`
- **THEN** el stock del producto con `id=5` se incrementa en 10

#### Scenario: Stock no se modifica si el detalle falla
- **WHEN** ocurre un error al insertar el `compra_detalle`
- **THEN** el stock del producto NO se modifica

### Requirement: Modelo TypeScript para compra_detalles
El frontend DEBE tener un campo `productoNombre?: string` en la interfaz `CompraDetalle`.

#### Scenario: Renderizado de nombre en tabla
- **WHEN** el frontend recibe el listado de compra_detalles
- **THEN** renderiza `productoNombre` en una columna de la tabla en lugar de mostrar el ID

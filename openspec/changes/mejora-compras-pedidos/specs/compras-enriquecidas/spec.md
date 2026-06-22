## ADDED Requirements

### Requirement: Listar compras con nombre de proveedor
El sistema DEBE devolver el nombre del proveedor (`proveedor_nombre`) en el listado de compras, obtenido mediante JOIN con la tabla `proveedores`.

#### Scenario: Listado incluye nombre del proveedor
- **WHEN** se invoca `GET /compras/`
- **THEN** cada compra en la respuesta incluye `proveedor_nombre: string` además de `proveedor_id: number`

#### Scenario: Proveedor no existe
- **WHEN** existe una compra cuyo `proveedor_id` no tiene registro correspondiente en `proveedores`
- **THEN** el sistema usa `!inner` JOIN, por lo que la compra NO se incluye en el listado

### Requirement: Modelo TypeScript para compras
El frontend DEBE tener un campo `proveedorNombre?: string` en la interfaz `Compra`.

#### Scenario: Renderizado de nombre en tabla
- **WHEN** el frontend recibe el listado de compras
- **THEN** renderiza `proveedorNombre` en una columna de la tabla en lugar de mostrar el ID

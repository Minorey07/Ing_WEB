## ADDED Requirements

### Requirement: Listar compras con detalles de productos
El sistema DEBE devolver los productos dentro de cada compra en `GET /compras/`.

#### Scenario: Compra con detalles
- **WHEN** se invoca `GET /compras/`
- **THEN** cada compra incluye un array `detalles` con `productoNombre`, `cantidad`, `precio`, `subtotal`

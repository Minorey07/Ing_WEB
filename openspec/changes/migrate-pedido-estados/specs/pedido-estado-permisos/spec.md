## ADDED Requirements

### Requirement: Backend valida rol antes de modificar estado de pedido
El backend SHALL validar que el usuario autenticado tenga rol ADMIN o ALMACENERO antes de procesar un cambio de estado en un pedido. Si el rol es VENDEDOR, SHALL rechazar la operación con HTTP 403.

#### Scenario: ADMIN actualiza estado de pedido
- **WHEN** un usuario con rol ADMIN envía `PUT /pedidos/{id}` con `estado_id` modificado
- **THEN** el backend SHALL permitir la modificación
- **AND** SHALL actualizar el registro en la tabla `pedidos`

#### Scenario: ALMACENERO actualiza estado de pedido
- **WHEN** un usuario con rol ALMACENERO envía `PUT /pedidos/{id}` con `estado_id` modificado
- **THEN** el backend SHALL permitir la modificación
- **AND** SHALL actualizar el registro en la tabla `pedidos`

#### Scenario: VENDEDOR intenta actualizar estado de pedido
- **WHEN** un usuario con rol VENDEDOR envía `PUT /pedidos/{id}` con cualquier cambio
- **THEN** el backend SHALL responder con HTTP 403 Forbidden
- **AND** SHALL NO modificar el registro

#### Scenario: VENDEDOR crea pedido nuevo
- **WHEN** un usuario con rol VENDEDOR envía `POST /pedidos/`
- **THEN** el backend SHALL permitir la creación normalmente
- **AND** SHALL asignar `estado_id` por defecto (PENDIENTE)

### Requirement: Frontend oculta control de estado al VENDEDOR
El frontend SHALL ocultar el selector de estado (dropdown o similar) cuando el usuario autenticado tenga rol VENDEDOR.

#### Scenario: VENDEDOR carga página de pedidos
- **WHEN** un usuario VENDEDOR carga el componente `pedido-component`
- **THEN** el selector de estado SHALL estar oculto
- **AND** el botón de guardar SHALL enviar el estado por defecto (PENDIENTE)

#### Scenario: ADMIN carga página de pedidos
- **WHEN** un usuario ADMIN carga el componente `pedido-component`
- **THEN** el selector de estado SHALL ser visible
- **AND** SHALL permitir seleccionar entre los estados disponibles

### Requirement: Flujo de estado controlado por estado_id
El estado del pedido SHALL manejarse exclusivamente mediante `estado_id` como clave foránea a la tabla `estados_pedido`, no como texto libre.

#### Scenario: Pedido creado con estado_id por defecto
- **WHEN** se crea un nuevo pedido
- **THEN** el sistema SHALL asignar `estado_id = 1` (PENDIENTE) automáticamente
- **AND** SHALL almacenar el ID numérico, no el texto del estado

#### Scenario: Consulta de pedido devuelve estado_id y nombre_estado
- **WHEN** el frontend lista pedidos
- **THEN** cada pedido SHALL incluir `estado_id` y el nombre del estado (obtenido del JOIN con `estados_pedido`)

# 📚 Documentación Backend - Normalización 3FN

## 🚀 Cambios Realizados

Se ha implementado la **normalización completa de la base de datos (3FN)** con nuevos repositorios, servicios y APIs para manejar catálogos y relaciones normalizadas.

---

## 📁 Estructura de Archivos Nuevos

### Repositorios (backend/repositorio/)
```
✅ categoria_repository.py              - 16 categorías de productos
✅ estado_producto_repository.py        - Estados: ACTIVO, AGOTADO, DESCONTINUADO, etc.
✅ estado_pedido_repository.py          - Estados: PENDIENTE, CONFIRMADO, EN_TRANSITO, ENTREGADO, etc.
✅ rol_repository.py                    - Roles: ADMIN, ALMACENERO, VENDEDOR
✅ ubicacion_local_repository.py        - Ubicaciones en Huancayo (5 predefinidas)
✅ ubicacion_nacional_repository.py     - Ubicaciones nacionales para proveedores (5 predefinidas)
✅ proveedor_repository.py              - Proveedores con FK a ubicacion_nacional
✅ serializador.py                      - Módulo para resolver FKs y serializar datos
```

### Servicios (backend/servicios/)
```
✅ categoria_service.py
✅ estado_producto_service.py
✅ estado_pedido_service.py
✅ rol_service.py
✅ ubicacion_local_service.py
✅ ubicacion_nacional_service.py
✅ proveedor_service.py                 - NUEVO (antes no existía)

🔄 ACTUALIZADOS:
   - producto_service.py               - Ahora usa serializador
   - usuario_service.py                - Ahora usa serializador
   - cliente_service.py                - Ahora usa serializador
   - pedido_service.py                 - Ahora usa serializador
```

### APIs (backend/apis/)
```
✅ categoria_api.py                     - GET/POST/PUT/DELETE /categorias
✅ estado_producto_api.py               - GET/POST/PUT/DELETE /estados-producto
✅ estado_pedido_api.py                 - GET/POST/PUT/DELETE /estados-pedido
✅ rol_api.py                           - GET/POST/PUT/DELETE /roles
✅ ubicacion_local_api.py               - GET/POST/PUT/DELETE /ubicaciones-locales
✅ ubicacion_nacional_api.py            - GET/POST/PUT/DELETE /ubicaciones-nacionales
✅ system_api.py                        - GET /inicializar, GET /status
```

### Inicialización
```
✅ inicializacion.py                    - Función para inicializar datos al arrancar
✅ main.py                              - ACTUALIZADO con nuevos routers
```

---

## 📊 Datos Iniciales Pre-poblados

### Categorías (16 tipos)
1. Enlatados
2. Productos Secos
3. Lácteos
4. Bebidas
5. Frutas y Verduras
6. Carnes
7. Panadería
8. Condimentos
9. Aceites y Grasas
10. Chocolates
11. Snacks
12. Congelados
13. Higiene
14. Dulces
15. Café y Té
16. Otros

### Estados de Producto
- ACTIVO (disponible)
- AGOTADO (sin stock)
- DESCONTINUADO
- EN_MANTENIMIENTO
- DAÑADO

### Estados de Pedido
- PENDIENTE
- CONFIRMADO
- EN_TRANSITO
- ENTREGADO (es_final=true)
- CANCELADO (es_final=true)
- DEVUELTO (es_final=true)

### Roles
- ADMIN (permisos: *)
- ALMACENERO (permisos: crear_producto, actualizar_producto, etc.)
- VENDEDOR (permisos: crear_pedido, ver_productos, etc.)

### Ubicaciones Locales (5 en Huancayo)
- Av. Giráldez 123
- Jr. Libertad 456
- Av. Ferrocarril 789
- Jr. Manco Cápac 321
- Av. Brasil 654

### Ubicaciones Nacionales (5 ciudades)
- Lima
- Arequipa
- Cusco
- Trujillo
- Ica

### Proveedores Iniciales (4)
- Distribuidora Peruana SAC
- Importaciones Andinas EIRL
- Comercializadora del Sur
- Productos Frescos Nacionales

---

## 🔗 Relaciones Normalizadas

### Producto
```
Producto {
    id, nombre, descripcion, precio, stock, presentacion,
    categoria_id → Categoria,
    estado_id → EstadoProducto
}
```

### Usuario
```
Usuario {
    id, nombre, correo, password,
    rol_id → Rol
}
```

### Cliente
```
Cliente {
    id, nombres,
    ubicacion_local_id → UbicacionLocal
}
```

### Proveedor
```
Proveedor {
    id, razonSocial, ruc,
    ubicacion_nacional_id → UbicacionNacional
}
```

### Pedido
```
Pedido {
    id, clienteId, vendedorId, fecha, total,
    estado_id → EstadoPedido,
    detalles → [PedidoDetalle]
}
```

---

## 🔄 Serialización de Datos

Todos los servicios usan el módulo `serializador.py` para resolver Foreign Keys **antes de enviar al frontend**.

### Ejemplo: Obtener Producto
**Request:** `GET /productos/1`

**Response:**
```json
{
  "id": 1,
  "nombre": "Arroz 50kg",
  "descripcion": "Arroz blanco premium",
  "precio": 120.50,
  "stock": 15,
  "presentacion": "Costal 50kg",
  "categoria_id": 2,
  "estado_id": 1,
  "categoria": {
    "id": 2,
    "nombre": "Productos Secos",
    "descripcion": "Granos, harinas y productos secos"
  },
  "estado": {
    "id": 1,
    "nombre": "ACTIVO",
    "descripcion": "Producto disponible para venta",
    "es_disponible": true
  }
}
```

---

## 🌐 Endpoints Disponibles

### Sistema
- `GET /status` - Estado del sistema
- `GET /inicializar` - Inicializar/verificar datos

### Categorías
- `GET /categorias` - Listar todas
- `GET /categorias/{id}` - Obtener por ID
- `POST /categorias` - Crear
- `PUT /categorias/{id}` - Actualizar
- `DELETE /categorias/{id}` - Eliminar

### Estados de Producto
- `GET /estados-producto` - Listar todos
- `GET /estados-producto/{id}` - Obtener por ID
- `GET /estados-producto/nombre/{nombre}` - Obtener por nombre
- `POST /estados-producto` - Crear
- `PUT /estados-producto/{id}` - Actualizar
- `DELETE /estados-producto/{id}` - Eliminar

### Estados de Pedido
- `GET /estados-pedido` - Listar todos
- `GET /estados-pedido/{id}` - Obtener por ID
- `GET /estados-pedido/nombre/{nombre}` - Obtener por nombre
- `POST /estados-pedido` - Crear
- `PUT /estados-pedido/{id}` - Actualizar
- `DELETE /estados-pedido/{id}` - Eliminar

### Roles
- `GET /roles` - Listar todos
- `GET /roles/{id}` - Obtener por ID
- `GET /roles/nombre/{nombre}` - Obtener por nombre
- `POST /roles` - Crear
- `PUT /roles/{id}` - Actualizar
- `DELETE /roles/{id}` - Eliminar

### Ubicaciones Locales
- `GET /ubicaciones-locales` - Listar todas
- `GET /ubicaciones-locales/{id}` - Obtener por ID
- `GET /ubicaciones-locales/distrito/{distrito}` - Filtrar por distrito
- `POST /ubicaciones-locales` - Crear
- `PUT /ubicaciones-locales/{id}` - Actualizar
- `DELETE /ubicaciones-locales/{id}` - Eliminar

### Ubicaciones Nacionales
- `GET /ubicaciones-nacionales` - Listar todas
- `GET /ubicaciones-nacionales/{id}` - Obtener por ID
- `GET /ubicaciones-nacionales/ciudad/{ciudad}` - Filtrar por ciudad
- `GET /ubicaciones-nacionales/departamento/{departamento}` - Filtrar por departamento
- `POST /ubicaciones-nacionales` - Crear
- `PUT /ubicaciones-nacionales/{id}` - Actualizar
- `DELETE /ubicaciones-nacionales/{id}` - Eliminar

### Productos (Actualizado)
- `GET /productos` - Listar con relaciones serializadas
- `GET /productos/{id}` - Obtener con relaciones serializadas
- Todos retornan `categoria` y `estado` resueltos

### Usuarios (Actualizado)
- `GET /usuarios` - Listar con rol serializado
- Todos retornan `rol` resuelto

### Clientes (Actualizado)
- `GET /clientes` - Listar con ubicación serializada
- Todos retornan `ubicacion` resuelta

### Pedidos (Actualizado)
- `GET /pedidos` - Listar con estado serializado
- Todos retornan `estado` resuelto

---

## ⚙️ Cómo Usar

### 1. Iniciar el servidor
```bash
cd backend
python -m uvicorn main:app --reload
```

### 2. Verificar status
```bash
curl http://localhost:8000/status
```

### 3. Inicializar datos
```bash
curl http://localhost:8000/inicializar
```

### 4. Obtener catálogos
```bash
# Categorías
curl http://localhost:8000/categorias

# Estados de producto
curl http://localhost:8000/estados-producto

# Roles
curl http://localhost:8000/roles

# Ubicaciones locales
curl http://localhost:8000/ubicaciones-locales
```

---

## 🔄 Flujo de Datos

```
Frontend (Angular)
    ↓ (Envía categoria_id=2, estado_id=1)
Backend API (producto_api.py)
    ↓
Servicio (producto_service.py)
    ↓ (Llama serializador)
Repositorio (producto_repository.py)
    ↓ (Obtiene productos)
    ↓
Serializador (serializador.py)
    ↓ (Resuelve FKs)
Repositorio (categoria_repository.py)
Repositorio (estado_producto_repository.py)
    ↓
Frontend (Recibe objeto completo con categoria y estado)
    ↓ (Accede a {{ producto.estado?.nombre }})
```

---

## ✨ Ventajas de la Nueva Estructura

✅ **Sin Redundancias** - Los datos se definen una sola vez  
✅ **Escalable** - Fácil agregar nuevos catálogos  
✅ **Consistencia** - No hay riesgo de inconsistencias  
✅ **Auditoría** - Se pueden rastrear cambios  
✅ **Reportes** - Mejor agregación de datos  
✅ **Frontend Compatible** - Serialización transparente  
✅ **3FN** - Cumple estándares de diseño de BD  

---

## 📋 Próximos Pasos

Cuando se integre con base de datos real (PostgreSQL, MySQL, etc.):

1. Reemplazar `*_repository.py` con consultas ORM (SQLAlchemy)
2. Mantener servicios y APIs sin cambios
3. Actualizar esquemas con columnas de tiempo (created_at, updated_at)
4. Agregar índices en FKs
5. Implementar transacciones en operaciones complejas

---

## 🛠️ Troubleshooting

### Error: "módulo no encontrado"
Asegúrate que los archivos están en:
- `backend/repositorio/`
- `backend/servicios/`
- `backend/apis/`

### Error: "FK no existe"
Verifica que:
- El ID de la categoría/estado existe
- Se enviaron los campos `_id` correctamente

### Error: "No se resuelve la relación"
El serializador requiere que los repositorios de relaciones existan.
Verifica `serializador.py` e importaciones en servicios.

---

## 📞 Contacto / Soporte

Para consultas sobre la normalización, ver:
- [GUIA_NORMALIZACION.md](../GUIA_NORMALIZACION.md) - Análisis detallado
- Comentarios en código de `serializador.py`

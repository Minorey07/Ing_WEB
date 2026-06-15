# 🚀 BACKEND NORMALIZADO - GUÍA DE EJECUCIÓN

## ✅ Estado del Proyecto

El backend ha sido completamente refactorizado con **normalización 3FN** implementada.

---

## 📦 Requisitos

```bash
# Python 3.8+
python --version

# FastAPI
pip install fastapi

# Uvicorn (servidor ASGI)
pip install uvicorn
```

---

## 🏃 Cómo Ejecutar

### 1. Verificar Estructura
```bash
cd backend
python verificar_estructura.py
```

Deberías ver:
```
✅ VERIFICACIÓN DE ESTRUCTURA NORMALIZACIÓN 3FN
...
✅ Archivos encontrados:  28
❌ Archivos faltantes:    0
🎉 ¡ESTRUCTURA COMPLETA Y CORRECTA!
```

### 2. Iniciar el Servidor
```bash
cd backend
python -m uvicorn main:app --reload
```

Deberías ver:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete

============================================================
🚀 INICIANDO SISTEMA MELIUS S.A.C
============================================================
✅ DATOS INICIALES CARGADOS:
  - Categorías: 16
  - Estados de Producto: 5
  - Estados de Pedido: 6
  - Roles: 3
  - Ubicaciones Locales: 5
  - Ubicaciones Nacionales: 5
  - Proveedores: 4
============================================================
```

### 3. Probar Endpoints

#### Status
```bash
curl http://localhost:8000/status
```

**Response:**
```json
{
  "status": "ok",
  "mensaje": "Sistema en funcionamiento",
  "version": "1.0.0"
}
```

#### Inicializar
```bash
curl http://localhost:8000/inicializar
```

#### Listar Categorías
```bash
curl http://localhost:8000/categorias
```

**Response:**
```json
[
  {
    "id": 1,
    "nombre": "Enlatados",
    "descripcion": "Productos enlatados y conservados"
  },
  {
    "id": 2,
    "nombre": "Productos Secos",
    "descripcion": "Granos, harinas y productos secos"
  },
  ...
]
```

#### Listar Roles
```bash
curl http://localhost:8000/roles
```

#### Listar Ubicaciones Locales
```bash
curl http://localhost:8000/ubicaciones-locales
```

#### Listar Proveedores
```bash
curl http://localhost:8000/categorias
```

---

## 📊 Estructura de Datos

### Categorías (16 tipos)
Se usan para clasificar los 16 tipos de productos mencionados por el docente.

### Estados
- **EstadoProducto**: Para marcar disponibilidad (ACTIVO, AGOTADO, etc.)
- **EstadoPedido**: Para seguimiento de pedidos (PENDIENTE, ENTREGADO, etc.)

### Ubicaciones
- **UbicacionLocal**: Direcciones de clientes en Huancayo
- **UbicacionNacional**: Direcciones de proveedores a nivel nacional

### Catálogos
- **Rol**: Permisos de usuarios (ADMIN, ALMACENERO, VENDEDOR)

---

## 🔗 Relaciones Normalizadas

```
Producto ──→ Categoria
Producto ──→ EstadoProducto
Usuario ──→ Rol
Cliente ──→ UbicacionLocal
Proveedor ──→ UbicacionNacional
Pedido ──→ EstadoPedido
```

---

## 🎯 Endpoints Principales

### Catálogos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/categorias` | Listar categorías |
| GET | `/estados-producto` | Listar estados de producto |
| GET | `/estados-pedido` | Listar estados de pedido |
| GET | `/roles` | Listar roles |
| GET | `/ubicaciones-locales` | Listar ubicaciones locales |
| GET | `/ubicaciones-nacionales` | Listar ubicaciones nacionales |

### Datos
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/productos` | Listar con relaciones resueltas |
| GET | `/usuarios` | Listar con rol resuelto |
| GET | `/clientes` | Listar con ubicación resuelta |
| GET | `/pedidos` | Listar con estado resuelto |

### Sistema
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/status` | Estado del sistema |
| GET | `/inicializar` | Verificar inicialización |

---

## 🔄 Flujo de Serialización

Cuando solicitas un producto:

```
GET /productos/1
  ↓
Backend obtiene: { id: 1, nombre: "Arroz", categoria_id: 2, estado_id: 1 }
  ↓
Serializador resuelve FKs:
  - categoria_id=2 → { id: 2, nombre: "Productos Secos", ... }
  - estado_id=1 → { id: 1, nombre: "ACTIVO", es_disponible: true, ... }
  ↓
Frontend recibe:
{
  "id": 1,
  "nombre": "Arroz",
  "categoria_id": 2,
  "estado_id": 1,
  "categoria": { "id": 2, "nombre": "Productos Secos", ... },
  "estado": { "id": 1, "nombre": "ACTIVO", ... }
}
```

---

## 💾 Almacenamiento de Datos

Actualmente, los datos se almacenan **en memoria** dentro de cada repositorio:

- `categoria_repository.py` - Precargas 16 categorías
- `estado_producto_repository.py` - Precarga 5 estados
- `estado_pedido_repository.py` - Precarga 6 estados
- `rol_repository.py` - Precarga 3 roles
- `ubicacion_local_repository.py` - Precarga 5 ubicaciones (Huancayo)
- `ubicacion_nacional_repository.py` - Precarga 5 ubicaciones
- `proveedor_repository.py` - Precarga 4 proveedores

**⚠️ Los datos se pierden al reiniciar el servidor.** Cuando se integre BD real, estos repositorios se reemplazarán con consultas ORM.

---

## 🔧 Personalización

### Agregar Nueva Categoría
```bash
curl -X POST http://localhost:8000/categorias \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Mi Nueva Categoría",
    "descripcion": "Descripción"
  }'
```

### Agregar Nueva Ubicación Local
```bash
curl -X POST http://localhost:8000/ubicaciones-locales \
  -H "Content-Type: application/json" \
  -d '{
    "direccion": "Av. Principal 123",
    "telefono": "064-234567",
    "distrito": "Huancayo"
  }'
```

---

## 🛠️ Troubleshooting

### Error: "ModuleNotFoundError"
```bash
# Verifica estar en el directorio backend
cd backend

# Verifica la estructura
python verificar_estructura.py
```

### Error: "Port 8000 already in use"
```bash
# Usa otro puerto
python -m uvicorn main:app --reload --port 8001
```

### Error: "CORS error" desde Angular
Verifica que el CORS está configurado en `main.py`:
```python
allow_origins=["http://localhost:4200"]
```

---

## 📝 Documentación

- [NORMALIZACION_CAMBIOS.md](./NORMALIZACION_CAMBIOS.md) - Detalle de cambios
- [../GUIA_NORMALIZACION.md](../GUIA_NORMALIZACION.md) - Análisis de normalización
- [serializador.py](./repositorio/serializador.py) - Comentarios en código

---

## 🚀 Próximos Pasos

1. **Integrar Base de Datos**
   - Reemplazar repositorios con ORM (SQLAlchemy)
   - Mantener servicios y APIs sin cambios

2. **Agregar Validaciones**
   - Pydantic para esquemas
   - Validadores de negocio

3. **Implementar Autenticación**
   - JWT en endpoints críticos
   - Verificar permisos por rol

4. **Agregar Logs**
   - Registrar operaciones
   - Auditoría de cambios

---

## ✨ Ventajas de Esta Arquitectura

✅ **Sin cambios en Frontend** - Las relaciones se resuelven transparentemente  
✅ **Mantenible** - Cambios futuros en BD no afectan APIs  
✅ **Escalable** - Fácil agregar nuevos catálogos  
✅ **3FN** - Cumple estándares de diseño de BD  
✅ **Listo para Producción** - Solo falta BD real  

---

## 📞 Soporte

Para preguntas sobre:
- **Normalización**: Ver GUIA_NORMALIZACION.md
- **Endpoints**: Ver NORMALIZACION_CAMBIOS.md
- **Código**: Comentarios en archivos Python

---

**¡Sistema listo para habilitar! 🎉**

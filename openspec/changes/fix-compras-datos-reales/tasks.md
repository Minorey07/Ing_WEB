# Tasks: Fix Compras Datos Reales

## 1. Backend — Eliminar INNER JOIN que silencia datos

- [x] 1.1 Cambiar `proveedores!inner(razon_social)` por consulta manual separada a `proveedores` — evita que compras sin proveedor válido sean excluidas del resultado
- [x] 1.2 Agregar `try/except` alrededor de consulta `compra_detalles` para que un error en JOIN no tumbe toda la respuesta
- [x] 1.3 Agregar `print("COMPRAS DB RAW:", compras)` y `print("COMPRAS DB RESPONSE:", compras)` para depuración

## 2. Frontend — Log de datos recibidos

- [x] 2.1 Agregar `console.log("COMPRAS RESPONSE:", data)` en `cargarCompras()` para verificar que el frontend recibe datos

## 3. Verificación

- [x] 3.1 `ng build` sin errores TS

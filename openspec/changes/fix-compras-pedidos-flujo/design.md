## Context

Compras solo muestran proveedor/total sin productos. Pedidos no se pueden editar. Estado_id se forza a 1 en creación ignorando input.

## Goals / Non-Goals

**Goals:** Compras con detalles anidados, pedidos editables, estado respetado en creación
**Non-Goals:** No cambiar estructura, no nuevas tablas, no romper roles

## Decisions

1. **JOIN anidado en compra_repository**: listar() obtiene compras + JOIN a proveedores, luego para cada compra hace JOIN a compra_detalles + productos
2. **PUT /pedidos/{id} existente**: se modifica el service para permitir edición completa (no solo estado) con validación de rol
3. **estado_id en POST**: si frontend envía estado_id, se respeta; si no, default 1

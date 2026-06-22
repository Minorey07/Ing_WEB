from repositorio import pedido_repository
from servicios import producto_service

def listar():
    return pedido_repository.listar()

def crear(pedido):
    for det in pedido.detalles:
        producto_service.descontar_stock(det.producto_id, det.cantidad)
    data = pedido.model_dump(exclude={"id"})
    data["detalles"] = [d.model_dump() for d in pedido.detalles]
    return pedido_repository.crear(data)

def actualizar_solo_estado(id: int, estado_id: int, rol_id: int):
    if rol_id not in (1, 2):
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"ok": False, "error": "Solo ADMIN y ALMACENERO pueden cambiar el estado del pedido"},
        )
    pedidos = pedido_repository.listar()
    pedido = next((p for p in pedidos if p["id"] == id), None)
    if not pedido:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"ok": False, "error": "Pedido no encontrado"},
        )
    if pedido.get("estado_id", 0) >= 2:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"ok": False, "error": "El pedido ya tiene un estado final"},
        )
    from db import supabase
    supabase.table("pedidos").update({"estado_id": estado_id}).eq("id", id).execute()
    pedido["estado_id"] = estado_id
    return pedido

def actualizar(pedido, rol_id: int = None):
    # ADMIN (1) y VENDEDOR (3) pueden editar pedido completo
    # ALMACENERO (2) solo puede cambiar estado (endpoint separado)
    if rol_id is not None and rol_id not in (1, 3):
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={"ok": False, "error": "No autorizado para editar pedidos"},
        )
    data = pedido.model_dump()
    data["detalles"] = [d.model_dump() for d in pedido.detalles]
    return pedido_repository.actualizar(data)

def eliminar(id):
    return pedido_repository.eliminar(id)

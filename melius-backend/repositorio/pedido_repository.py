from db import supabase

PEDIDOS_TABLE = "pedidos"
DETALLES_TABLE = "pedido_detalles"

def listar():
    resp = supabase.table(PEDIDOS_TABLE).select("*, estados_pedido!inner(nombre), clientes!inner(nombres), usuarios!inner(nombre)").order("id").execute()
    pedidos = resp.data or []
    for p in pedidos:
        p["estado_nombre"] = p.pop("estados_pedido", {}).get("nombre") if p.get("estados_pedido") else None
        p["cliente_nombre"] = p.pop("clientes", {}).get("nombres") if p.get("clientes") else None
        p["vendedor_nombre"] = p.pop("usuarios", {}).get("nombre") if p.get("usuarios") else None
        det_resp = supabase.table(DETALLES_TABLE).select("*, productos!inner(nombre)").eq("pedido_id", p["id"]).execute()
        for d in det_resp.data or []:
            d["producto_nombre"] = d.pop("productos", {}).get("nombre") if d.get("productos") else None
        p["detalles"] = det_resp.data or []
    return pedidos

def crear(pedido_data: dict):
    detalles = pedido_data.pop("detalles", [])
    pedido_data.pop("estado_nombre", None)
    resp = supabase.table(PEDIDOS_TABLE).insert(pedido_data).execute()
    if not resp.data:
        return None
    pedido = resp.data[0]
    pedido_id = pedido["id"]
    for det in detalles:
        det["pedido_id"] = pedido_id
        supabase.table(DETALLES_TABLE).insert(det).execute()
    det_resp = supabase.table(DETALLES_TABLE).select("*, productos!inner(nombre)").eq("pedido_id", pedido_id).execute()
    for d in det_resp.data or []:
        d["producto_nombre"] = d.pop("productos", {}).get("nombre") if d.get("productos") else None
    pedido["detalles"] = det_resp.data or []
    pedido["estado_nombre"] = None
    return pedido

def actualizar(pedido_data: dict):
    pedido_id = pedido_data.pop("id")
    detalles = pedido_data.pop("detalles", [])
    pedido_data.pop("estado_nombre", None)
    supabase.table(PEDIDOS_TABLE).update(pedido_data).eq("id", pedido_id).execute()
    supabase.table(DETALLES_TABLE).delete().eq("pedido_id", pedido_id).execute()
    for det in detalles:
        det["pedido_id"] = pedido_id
        supabase.table(DETALLES_TABLE).insert(det).execute()
    det_resp = supabase.table(DETALLES_TABLE).select("*, productos!inner(nombre)").eq("pedido_id", pedido_id).execute()
    for d in det_resp.data or []:
        d["producto_nombre"] = d.pop("productos", {}).get("nombre") if d.get("productos") else None
    pedido_data["id"] = pedido_id
    pedido_data["detalles"] = det_resp.data or []
    return pedido_data

def eliminar(id: int):
    supabase.table(DETALLES_TABLE).delete().eq("pedido_id", id).execute()
    supabase.table(PEDIDOS_TABLE).delete().eq("id", id).execute()

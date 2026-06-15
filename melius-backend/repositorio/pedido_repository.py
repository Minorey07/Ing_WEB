from db import supabase

PEDIDOS_TABLE = "pedidos"
DETALLES_TABLE = "pedido_detalles"

def listar():
    resp = supabase.table(PEDIDOS_TABLE).select("*").order("id").execute()
    pedidos = resp.data or []
    for p in pedidos:
        det_resp = supabase.table(DETALLES_TABLE).select("*").eq("pedido_id", p["id"]).execute()
        p["detalles"] = det_resp.data or []
    return pedidos

def crear(pedido_data: dict):
    detalles = pedido_data.pop("detalles", [])
    resp = supabase.table(PEDIDOS_TABLE).insert(pedido_data).execute()
    if not resp.data:
        return None
    pedido = resp.data[0]
    pedido_id = pedido["id"]
    for det in detalles:
        det["pedido_id"] = pedido_id
        supabase.table(DETALLES_TABLE).insert(det).execute()
    det_resp = supabase.table(DETALLES_TABLE).select("*").eq("pedido_id", pedido_id).execute()
    pedido["detalles"] = det_resp.data or []
    return pedido

def actualizar(pedido_data: dict):
    pedido_id = pedido_data.pop("id")
    detalles = pedido_data.pop("detalles", [])
    supabase.table(PEDIDOS_TABLE).update(pedido_data).eq("id", pedido_id).execute()
    supabase.table(DETALLES_TABLE).delete().eq("pedido_id", pedido_id).execute()
    for det in detalles:
        det["pedido_id"] = pedido_id
        supabase.table(DETALLES_TABLE).insert(det).execute()
    det_resp = supabase.table(DETALLES_TABLE).select("*").eq("pedido_id", pedido_id).execute()
    pedido_data["id"] = pedido_id
    pedido_data["detalles"] = det_resp.data or []
    return pedido_data

def eliminar(id: int):
    supabase.table(DETALLES_TABLE).delete().eq("pedido_id", id).execute()
    supabase.table(PEDIDOS_TABLE).delete().eq("id", id).execute()

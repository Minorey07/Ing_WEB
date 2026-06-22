from db import supabase

TABLE = "compras"

def listar():
    compras_resp = supabase.table(TABLE).select("*").order("id").execute()
    compras = compras_resp.data or []
    print("COMPRAS DB RAW:", compras)
    for c in compras:
        prov_resp = supabase.table("proveedores").select("razon_social").eq("id", c["proveedor_id"]).execute()
        prov_data = prov_resp.data[0] if prov_resp.data else None
        c["proveedor_nombre"] = prov_data["razon_social"] if prov_data else None
        det_resp = supabase.table("compra_detalles").select("*").eq("compra_id", c["id"]).execute()
        detalles = det_resp.data or []
        for d in detalles:
            prod_resp = supabase.table("productos").select("nombre").eq("id", d["producto_id"]).execute()
            prod_data = prod_resp.data[0] if prod_resp.data else None
            d["producto_nombre"] = prod_data["nombre"] if prod_data else None
        c["detalles"] = detalles
    print("COMPRAS DB RESPONSE:", compras)
    return compras

def crear(c):
    data = c.model_dump(exclude={"id", "created_at", "proveedor_nombre", "detalles"})
    resp = supabase.table(TABLE).insert(data).execute()
    return resp.data[0] if resp.data else None

def actualizar(c):
    data = c.model_dump(exclude={"id", "created_at", "proveedor_nombre", "detalles"})
    supabase.table(TABLE).update(data).eq("id", c.id).execute()
    return c

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

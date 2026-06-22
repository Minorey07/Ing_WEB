from db import supabase

TABLE = "compra_detalles"

def listar():
    resp = supabase.table(TABLE).select("*").order("id").execute()
    detalles = resp.data or []
    for d in detalles:
        prod_resp = supabase.table("productos").select("nombre").eq("id", d["producto_id"]).execute()
        prod_data = prod_resp.data[0] if prod_resp.data else None
        d["producto_nombre"] = prod_data["nombre"] if prod_data else None
    return detalles

def crear(data: dict):
    resp = supabase.table(TABLE).insert(data).execute()
    return resp.data[0] if resp.data else None

def actualizar(c):
    data = c.model_dump(exclude={"id", "producto_nombre"})
    supabase.table(TABLE).update(data).eq("id", c.id).execute()
    return c

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

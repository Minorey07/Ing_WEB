from db import supabase

TABLE = "productos"

def listar():
    resp = supabase.table(TABLE).select("*, estados_producto!inner(nombre), categorias(nombre)").order("id").execute()
    for p in resp.data or []:
        p["estado_nombre"] = p.pop("estados_producto", {}).get("nombre") if p.get("estados_producto") else None
        p["categoria_nombre"] = p.pop("categorias", {}).get("nombre") if p.get("categorias") else None
    return resp.data

def crear(p):
    data = p.model_dump(exclude={"id", "estado_nombre", "categoria_nombre"})
    resp = supabase.table(TABLE).insert(data).execute()
    if resp.data:
        nuevo = resp.data[0]
        nuevo["estado_nombre"] = None
        nuevo["categoria_nombre"] = None
        return nuevo
    return None

def actualizar(p):
    data = p.model_dump(exclude={"id", "estado_nombre", "categoria_nombre"})
    supabase.table(TABLE).update(data).eq("id", p.id).execute()
    return p

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

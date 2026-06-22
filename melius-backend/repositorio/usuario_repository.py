from db import supabase

TABLE = "usuarios"

def listar():
    resp = supabase.table(TABLE).select("*, roles!inner(nombre)").order("id").execute()
    for u in resp.data or []:
        u["rol_nombre"] = u.pop("roles", {}).get("nombre") if u.get("roles") else None
    return resp.data

def crear(u):
    data = u.model_dump(exclude={"id", "rol_nombre"})
    resp = supabase.table(TABLE).insert(data).execute()
    if resp.data:
        nuevo = resp.data[0]
        nuevo["rol_nombre"] = None
        return nuevo
    return None

def actualizar(u):
    data = u.model_dump(exclude={"id", "rol_nombre"})
    supabase.table(TABLE).update(data).eq("id", u.id).execute()
    return u

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

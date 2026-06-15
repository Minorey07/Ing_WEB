from db import supabase

TABLE = "productos"

def listar():
    resp = supabase.table(TABLE).select("*").order("id").execute()
    return resp.data

def crear(p):
    data = p.model_dump(exclude={"id"})
    resp = supabase.table(TABLE).insert(data).execute()
    return resp.data[0] if resp.data else None

def actualizar(p):
    data = p.model_dump(exclude={"id"})
    supabase.table(TABLE).update(data).eq("id", p.id).execute()
    return p

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

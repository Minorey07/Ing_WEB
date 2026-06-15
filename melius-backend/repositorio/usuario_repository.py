from db import supabase

TABLE = "usuarios"

def listar():
    resp = supabase.table(TABLE).select("*").order("id").execute()
    return resp.data

def crear(u):
    data = u.model_dump(exclude={"id"})
    resp = supabase.table(TABLE).insert(data).execute()
    return resp.data[0] if resp.data else None

def actualizar(u):
    data = u.model_dump(exclude={"id"})
    supabase.table(TABLE).update(data).eq("id", u.id).execute()
    return u

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

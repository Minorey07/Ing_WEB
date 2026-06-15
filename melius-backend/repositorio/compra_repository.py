from db import supabase

TABLE = "compras"

def listar():
    resp = supabase.table(TABLE).select("*").order("id").execute()
    return resp.data

def crear(c):
    data = c.model_dump(exclude={"id", "created_at"})
    resp = supabase.table(TABLE).insert(data).execute()
    return resp.data[0] if resp.data else None

def actualizar(c):
    data = c.model_dump(exclude={"id", "created_at"})
    supabase.table(TABLE).update(data).eq("id", c.id).execute()
    return c

def eliminar(id: int):
    supabase.table(TABLE).delete().eq("id", id).execute()

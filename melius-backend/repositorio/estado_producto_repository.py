from db import supabase

TABLE = "estados_producto"

def listar():
    resp = supabase.table(TABLE).select("*").order("id").execute()
    return resp.data

from db import supabase

TABLE = "estados_pedido"

def listar():
    resp = supabase.table(TABLE).select("*").order("id").execute()
    return resp.data

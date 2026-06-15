from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis import (
    cliente_api,
    producto_api,
    pedido_api,
    usuario_api,
    dashboard_api,
    auth_api,
    proveedor_api,
    compra_api,
)

app = FastAPI(title="Melius S.A.C API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_api.router)
app.include_router(cliente_api.router)
app.include_router(producto_api.router)
app.include_router(pedido_api.router)
app.include_router(usuario_api.router)
app.include_router(proveedor_api.router)
app.include_router(compra_api.router)
app.include_router(dashboard_api.router)

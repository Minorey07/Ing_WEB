from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis import (
    cliente_api,
    producto_api,
    pedido_api,
    usuario_api,
    proveedor_api,
    dashboard_api,
    # Nuevas APIs de catálogos
    categoria_api,
    estado_producto_api,
    estado_pedido_api,
    rol_api,
    ubicacion_local_api,
    ubicacion_nacional_api,
    system_api
)

from inicializacion import inicializar_datos

app = FastAPI(title="Melius S.A.C API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers existentes
app.include_router(cliente_api.router)
app.include_router(producto_api.router)
app.include_router(pedido_api.router)
app.include_router(usuario_api.router)
app.include_router(proveedor_api.router)
app.include_router(dashboard_api.router)

# Routers de catálogos
app.include_router(categoria_api.router)
app.include_router(estado_producto_api.router)
app.include_router(estado_pedido_api.router)
app.include_router(rol_api.router)
app.include_router(ubicacion_local_api.router)
app.include_router(ubicacion_nacional_api.router)

# Router de sistema
app.include_router(system_api.router)

# Inicializar datos al arrancar
@app.on_event("startup")
async def startup_event():
    """Se ejecuta al iniciar la aplicación"""
    print("\n" + "="*60)
    print("🚀 INICIANDO SISTEMA MELIUS S.A.C")
    print("="*60)
    inicializar_datos()
    print("="*60 + "\n")
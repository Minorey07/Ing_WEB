from fastapi import FastAPI
from inicializacion import obtener_estado_inicial

router = FastAPI()

@router.get("/inicializar")
def inicializar():
    """Inicializa los datos del sistema"""
    return obtener_estado_inicial()

@router.get("/status")
def status():
    """Obtiene el estado del sistema"""
    return {
        "status": "ok",
        "mensaje": "Sistema en funcionamiento",
        "version": "1.0.0"
    }

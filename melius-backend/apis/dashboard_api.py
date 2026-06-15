from fastapi import APIRouter
from servicios import dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/resumen")
def resumen():
    return dashboard_service.resumen()
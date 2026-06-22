from fastapi import APIRouter, Depends

from auth.dependencies import get_current_user
from servicios import dashboard_service

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/resumen")
def resumen(current_user: dict = Depends(get_current_user)):
    data = dashboard_service.resumen()
    return {"ok": True, "data": data}

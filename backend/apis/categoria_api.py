from fastapi import FastAPI, HTTPException
from esquema.categoria import Categoria
from servicios import categoria_service

router = FastAPI()

@router.get("/categorias")
def obtener_todas_categorias():
    """Obtiene todas las categorías"""
    return categoria_service.listar()

@router.get("/categorias/{id}")
def obtener_categoria(id: int):
    """Obtiene una categoría por ID"""
    categoria = categoria_service.obtener_por_id(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria

@router.post("/categorias")
def crear_categoria(categoria: Categoria):
    """Crea una nueva categoría"""
    return categoria_service.crear(categoria)

@router.put("/categorias/{id}")
def actualizar_categoria(id: int, categoria: Categoria):
    """Actualiza una categoría"""
    categoria.id = id
    resultado = categoria_service.actualizar(categoria)
    if not resultado:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return resultado

@router.delete("/categorias/{id}")
def eliminar_categoria(id: int):
    """Elimina una categoría"""
    categoria = categoria_service.obtener_por_id(id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    categoria_service.eliminar(id)
    return {"mensaje": "Categoría eliminada exitosamente"}

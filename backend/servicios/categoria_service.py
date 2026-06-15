from repositorio import categoria_repository
from esquema.categoria import Categoria

def listar():
    """Lista todas las categorías"""
    return categoria_repository.listar()

def obtener_por_id(id: int):
    """Obtiene una categoría por ID"""
    return categoria_repository.obtener_por_id(id)

def crear(categoria: Categoria):
    """Crea una nueva categoría"""
    return categoria_repository.crear(categoria)

def actualizar(categoria: Categoria):
    """Actualiza una categoría"""
    return categoria_repository.actualizar(categoria)

def eliminar(id: int):
    """Elimina una categoría"""
    categoria_repository.eliminar(id)

from esquema.categoria import Categoria

# Base de datos en memoria - Categorías (16 tipos iniciales)
categorias = [
    Categoria(id=1, nombre="Enlatados", descripcion="Productos enlatados y conservados"),
    Categoria(id=2, nombre="Productos Secos", descripcion="Granos, harinas y productos secos"),
    Categoria(id=3, nombre="Lácteos", descripcion="Leche, queso y derivados lácteos"),
    Categoria(id=4, nombre="Bebidas", descripcion="Bebidas y refrescos"),
    Categoria(id=5, nombre="Frutas y Verduras", descripcion="Produce fresco"),
    Categoria(id=6, nombre="Carnes", descripcion="Carnes y embutidos"),
    Categoria(id=7, nombre="Panadería", descripcion="Pan y productos de panadería"),
    Categoria(id=8, nombre="Condimentos", descripcion="Especias y condimentos"),
    Categoria(id=9, nombre="Aceites y Grasas", descripcion="Aceites de cocina"),
    Categoria(id=10, nombre="Chocolates", descripcion="Chocolate y cacao"),
    Categoria(id=11, nombre="Snacks", descripcion="Aperitivos y snacks"),
    Categoria(id=12, nombre="Congelados", descripcion="Productos congelados"),
    Categoria(id=13, nombre="Higiene", descripcion="Productos de higiene y limpieza"),
    Categoria(id=14, nombre="Dulces", descripcion="Dulces y confitería"),
    Categoria(id=15, nombre="Café y Té", descripcion="Café, té y infusiones"),
    Categoria(id=16, nombre="Otros", descripcion="Otros productos")
]

def listar():
    """Retorna todas las categorías"""
    return categorias

def obtener_por_id(id: int):
    """Obtiene una categoría por ID"""
    for c in categorias:
        if c.id == id:
            return c
    return None

def crear(categoria: Categoria):
    """Crea una nueva categoría"""
    nueva_id = max([c.id for c in categorias], default=0) + 1
    categoria.id = nueva_id
    categorias.append(categoria)
    return categoria

def actualizar(categoria: Categoria):
    """Actualiza una categoría existente"""
    for i, c in enumerate(categorias):
        if c.id == categoria.id:
            categorias[i] = categoria
            return categoria
    return None

def eliminar(id: int):
    """Elimina una categoría por ID"""
    global categorias
    categorias = [c for c in categorias if c.id != id]

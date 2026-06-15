from esquema.ubicacion_local import UbicacionLocal

# Base de datos en memoria - Ubicaciones Locales (Huancayo)
ubicaciones_locales = [
    UbicacionLocal(id=1, direccion="Av. Giráldez 123", telefono="064-234567", distrito="Huancayo"),
    UbicacionLocal(id=2, direccion="Jr. Libertad 456", telefono="064-234568", distrito="Huancayo"),
    UbicacionLocal(id=3, direccion="Av. Ferrocarril 789", telefono="064-234569", distrito="Huancayo"),
    UbicacionLocal(id=4, direccion="Jr. Manco Cápac 321", telefono="064-234570", distrito="Huancayo"),
    UbicacionLocal(id=5, direccion="Av. Brasil 654", telefono="064-234571", distrito="Huancayo"),
]

def listar():
    """Retorna todas las ubicaciones locales"""
    return ubicaciones_locales

def obtener_por_id(id: int):
    """Obtiene una ubicación por ID"""
    for u in ubicaciones_locales:
        if u.id == id:
            return u
    return None

def obtener_por_distrito(distrito: str):
    """Obtiene ubicaciones por distrito"""
    return [u for u in ubicaciones_locales if u.distrito.lower() == distrito.lower()]

def crear(ubicacion: UbicacionLocal):
    """Crea una nueva ubicación"""
    nueva_id = max([u.id for u in ubicaciones_locales], default=0) + 1
    ubicacion.id = nueva_id
    ubicaciones_locales.append(ubicacion)
    return ubicacion

def actualizar(ubicacion: UbicacionLocal):
    """Actualiza una ubicación existente"""
    for i, u in enumerate(ubicaciones_locales):
        if u.id == ubicacion.id:
            ubicaciones_locales[i] = ubicacion
            return ubicacion
    return None

def eliminar(id: int):
    """Elimina una ubicación por ID"""
    global ubicaciones_locales
    ubicaciones_locales = [u for u in ubicaciones_locales if u.id != id]

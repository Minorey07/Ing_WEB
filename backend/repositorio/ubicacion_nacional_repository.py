from esquema.ubicacion_nacional import UbicacionNacional

# Base de datos en memoria - Ubicaciones Nacionales (Proveedores)
ubicaciones_nacionales = [
    UbicacionNacional(id=1, direccion="Av. Arenales 1234", telefono="01-2345678", ciudad="Lima", departamento="Lima", pais="Perú"),
    UbicacionNacional(id=2, direccion="Jr. Principal 567", telefono="041-234567", ciudad="Arequipa", departamento="Arequipa", pais="Perú"),
    UbicacionNacional(id=3, direccion="Av. Comercio 890", telefono="084-234567", ciudad="Cusco", departamento="Cusco", pais="Perú"),
    UbicacionNacional(id=4, direccion="Jr. Industrial 321", telefono="033-234567", ciudad="Trujillo", departamento="La Libertad", pais="Perú"),
    UbicacionNacional(id=5, direccion="Av. Empresa 654", telefono="056-234567", ciudad="Ica", departamento="Ica", pais="Perú"),
]

def listar():
    """Retorna todas las ubicaciones nacionales"""
    return ubicaciones_nacionales

def obtener_por_id(id: int):
    """Obtiene una ubicación por ID"""
    for u in ubicaciones_nacionales:
        if u.id == id:
            return u
    return None

def obtener_por_ciudad(ciudad: str):
    """Obtiene ubicaciones por ciudad"""
    return [u for u in ubicaciones_nacionales if u.ciudad.lower() == ciudad.lower()]

def obtener_por_departamento(departamento: str):
    """Obtiene ubicaciones por departamento"""
    return [u for u in ubicaciones_nacionales if u.departamento.lower() == departamento.lower()]

def crear(ubicacion: UbicacionNacional):
    """Crea una nueva ubicación"""
    nueva_id = max([u.id for u in ubicaciones_nacionales], default=0) + 1
    ubicacion.id = nueva_id
    ubicaciones_nacionales.append(ubicacion)
    return ubicacion

def actualizar(ubicacion: UbicacionNacional):
    """Actualiza una ubicación existente"""
    for i, u in enumerate(ubicaciones_nacionales):
        if u.id == ubicacion.id:
            ubicaciones_nacionales[i] = ubicacion
            return ubicacion
    return None

def eliminar(id: int):
    """Elimina una ubicación por ID"""
    global ubicaciones_nacionales
    ubicaciones_nacionales = [u for u in ubicaciones_nacionales if u.id != id]

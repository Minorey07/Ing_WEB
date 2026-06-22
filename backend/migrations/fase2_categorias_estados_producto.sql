-- Fase 2: Categorías, Estados Producto, Productos FK
-- Ejecutar en orden dentro del SQL Editor de Supabase

-- T2.1: Crear tabla categorias
CREATE TABLE IF NOT EXISTS categorias (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL,
    descripcion TEXT
);

-- T2.2: Crear tabla estados_producto
CREATE TABLE IF NOT EXISTS estados_producto (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL
);

-- T2.3: Insertar seed
INSERT INTO estados_producto (id, nombre) VALUES (1, 'ACTIVO'), (2, 'INACTIVO')
ON CONFLICT (id) DO NOTHING;

-- T2.4: Agregar productos.categoria_id
ALTER TABLE productos ADD COLUMN IF NOT EXISTS categoria_id BIGINT REFERENCES categorias(id);

-- T2.5: Agregar productos.estado_id, migrar datos
ALTER TABLE productos ADD COLUMN IF NOT EXISTS estado_id BIGINT REFERENCES estados_producto(id) DEFAULT 1;
UPDATE productos SET estado_id = (SELECT id FROM estados_producto WHERE estados_producto.nombre = productos.estado);
ALTER TABLE productos ALTER COLUMN estado_id SET NOT NULL;
ALTER TABLE productos ALTER COLUMN estado_id SET DEFAULT 1;

-- T2.6: Eliminar productos.estado
ALTER TABLE productos DROP COLUMN IF EXISTS estado;

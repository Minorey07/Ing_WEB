-- Fase 1: Roles, Estados Pedido, Usuarios/Pedidos FK
-- Ejecutar en orden dentro del SQL Editor de Supabase

-- T1.1: Crear tabla roles
CREATE TABLE IF NOT EXISTS roles (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL
);

-- T1.2: Insertar seed data
INSERT INTO roles (id, nombre) VALUES (1, 'ADMIN'), (2, 'ALMACENERO'), (3, 'VENDEDOR')
ON CONFLICT (id) DO NOTHING;

-- T1.3: Crear tabla estados_pedido
CREATE TABLE IF NOT EXISTS estados_pedido (
    id BIGSERIAL PRIMARY KEY,
    nombre TEXT UNIQUE NOT NULL
);

-- T1.4: Insertar seed data
INSERT INTO estados_pedido (id, nombre) VALUES (1, 'PENDIENTE'), (2, 'ENTREGADO')
ON CONFLICT (id) DO NOTHING;

-- T1.5: Agregar usuarios.rol_id, migrar datos
ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS rol_id BIGINT REFERENCES roles(id);
UPDATE usuarios SET rol_id = (SELECT id FROM roles WHERE roles.nombre = usuarios.rol);
ALTER TABLE usuarios ALTER COLUMN rol_id SET NOT NULL;

-- T1.6: Eliminar usuarios.rol
ALTER TABLE usuarios DROP COLUMN IF EXISTS rol;

-- T1.7: Agregar pedidos.estado_id, migrar datos
ALTER TABLE pedidos ADD COLUMN IF NOT EXISTS estado_id BIGINT REFERENCES estados_pedido(id) DEFAULT 1;
UPDATE pedidos SET estado_id = (SELECT id FROM estados_pedido WHERE estados_pedido.nombre = pedidos.estado);
ALTER TABLE pedidos ALTER COLUMN estado_id SET NOT NULL;
ALTER TABLE pedidos ALTER COLUMN estado_id SET DEFAULT 1;

-- T1.8: Eliminar pedidos.estado
ALTER TABLE pedidos DROP COLUMN IF EXISTS estado;

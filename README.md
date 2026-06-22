# Melius SAC - Sistema de Gestión ERP

Sistema de gestión empresarial para Melius SAC construido con **Angular 21** (frontend), **FastAPI** (backend) y **Supabase** (base de datos).

## Arquitectura

```
┌─────────────────────────────────────────────────────┐
│                  Angular 21 (Frontend)              │
│  http://localhost:4200                              │
│  Programa_Final_Frontend/                           │
└──────────────────────┬──────────────────────────────┘
                       │ HTTP (JSON)
                       ▼
┌─────────────────────────────────────────────────────┐
│              FastAPI (Backend)                       │
│  http://localhost:8000                               │
│  melius-backend/                                    │
└──────────────────────┬──────────────────────────────┘
                       │ supabase-py
                       ▼
┌─────────────────────────────────────────────────────┐
│              Supabase (PostgreSQL)                   │
│  Base de datos en la nube                           │
└─────────────────────────────────────────────────────┘
```

## Requisitos

- **Python** >= 3.11
- **Node.js** >= 20.x
- **npm** >= 11.x
- **Angular CLI** 21.2.x (`npm install -g @angular/cli`)
- Una cuenta en [Supabase](https://supabase.com)

---

## Instalación - Backend (FastAPI)

### 1. Clonar el repositorio

```bash
git clone <repo-url>
cd melius-sac
```

### 2. Configurar variables de entorno

```bash
cd melius-backend
cp .env.example .env
```

Editar `.env` con tus credenciales de Supabase:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
JWT_SECRET=melius-sac-secret-key-2024
JWT_ALGORITHM=HS256
```

> `JWT_SECRET` puede ser cualquier string. Se usa para firmar los tokens JWT.

### 3. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Configurar base de datos en Supabase

1. Crear un proyecto en [Supabase](https://supabase.com)
2. Ir a **SQL Editor**
3. Ejecutar los scripts de migración en orden:

   - `melius-backend/migrations/fase1_roles_estados_pedido.sql`
   - `melius-backend/migrations/fase2_categorias_estados_producto.sql`

4. Copiar las credenciales (`Project URL` y `anon public key`) al `.env`

### 5. Ejecutar backend

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

El backend estará disponible en: `http://localhost:8000`

Documentación Swagger: `http://localhost:8000/docs`

---

## Instalación - Frontend (Angular)

### 1. Instalar dependencias

```bash
cd Programa_Final_Frontend
npm install
```

### 2. Ejecutar en desarrollo

```bash
ng serve
```

El frontend estará disponible en: `http://localhost:4200`

### 3. Build de producción

```bash
ng build
```

Los archivos generados estarán en `dist/Programa_Final_Frontend/`.

---

## Credenciales de ejemplo

| Rol | Correo | Contraseña |
|---|---|---|
| ADMIN | admin@melius.com | 123 |
| ALMACENERO | almacenero@melius.com | 123 |
| VENDEDOR | vendedor@melius.com | 123 |

> Estas credenciales deben ser insertadas directamente en la tabla `usuarios` de Supabase con la contraseña hasheada.

---

## Dependencias principales

### Backend (Python)

| Paquete | Versión mínima |
|---|---|
| fastapi | >=0.110 |
| uvicorn | >=0.27 |
| supabase | >=2.0 |
| python-jose | >=3.3 (con cryptography) |
| python-dotenv | >=1.0 |
| pydantic | >=2.0 |

### Frontend (Angular/NPM)

| Paquete | Versión |
|---|---|
| @angular/core | ^21.2.0 |
| @angular/cli | ^21.2.7 |
| chart.js | ^4.5.1 |
| ng2-charts | ^10.0.0 |
| camelcase-keys | ^10.0.2 |
| snakecase-keys | ^9.0.2 |
| rxjs | ~7.8.0 |
| typescript | ^5.4.5 |

---

## Estructura del proyecto

```
melius-sac/
├── melius-backend/               # Backend FastAPI
│   ├── apis/                     # Rutas / endpoints
│   ├── auth/                     # Autenticación JWT
│   ├── esquema/                  # Schemas Pydantic
│   ├── migrations/               # SQL de migración
│   ├── repositorio/              # Capa de datos (Supabase)
│   ├── servicios/                # Lógica de negocio
│   ├── config.py                 # Config desde .env
│   ├── db.py                     # Cliente Supabase
│   ├── main.py                   # Entry point
│   ├── pyproject.toml            # Dependencias Python
│   └── requirements.txt          # Dependencias exportadas
│
├── Programa_Final_Frontend/      # Frontend Angular
│   └── src/app/
│       ├── features/             # Componentes por módulo
│       ├── layout/               # Sidebar, navbar
│       ├── models/               # Interfaces TypeScript
│       └── services/             # Servicios HTTP
│
└── README.md                     # Este archivo
```

# 🚀 Guía de Despliegue en Render

## Resumen del Proyecto
- **Backend:** FastAPI (Python) en puerto 8000
- **Frontend:** Angular con SSR (Node.js) en puerto 3000+
- **Proxy:** Express middleware para conectar ambos servicios
- **Base de datos:** Supabase
- **Despliegue:** UN ÚNICO Web Service en Render

---

## 📋 Checklist Previo al Despliegue

- [ ] Repositorio en GitHub
- [ ] Variables de entorno configuradas
- [ ] Base de datos Supabase creada
- [ ] JWT_SECRET generado (usa `openssl rand -hex 32`)
- [ ] Cuenta en [Render.com](https://render.com)

---

## 🔧 Configuración Paso a Paso

### 1️⃣ Prepara tu Repositorio

Los archivos necesarios ya están creados:
- `render.yaml` ✅ - Configuración automática para Render
- `.env.example` ✅ - Plantilla de variables de entorno
- `start-unified.sh` ✅ - Script que inicia backend + frontend
- `Programa_Final_Frontend/server-proxy.js` ✅ - Servidor proxy Express
- `melius-backend/requirements.txt` ✅ - Actualizado con dependencias
- `melius-backend/main.py` ✅ - Configurado con CORS dinámico
- `Programa_Final_Frontend/package.json` ✅ - Incluye http-proxy-middleware

**Haz commit y push:**
```bash
git add .
git commit -m "Configuración de despliegue unificado en Render"
git push origin version-despliegue
```

### 2️⃣ Crea el Servicio en Render

#### **Opción A: Usar render.yaml (RECOMENDADO)**
1. Ve a [https://dashboard.render.com](https://dashboard.render.com)
2. Haz clic en "New +" → "Blueprint"
3. Conecta tu repositorio GitHub
4. Selecciona la rama `version-despliegue`
5. Render automáticamente leerá `render.yaml` y creará el servicio
6. Llena las variables de entorno (ver abajo)
7. Despliega

#### **Opción B: Crear Servicio Manualmente**

1. Click "New +" → "Web Service"
2. **Name:** `melius`
3. **Build Command:** 
   ```
   cd melius-backend && pip install -r requirements.txt && cd .. && cd Programa_Final_Frontend && npm install && npm run build && cd ..
   ```
4. **Start Command:** 
   ```
   bash ./start-unified.sh
   ```
5. **Environment Variables:**
   ```
   DATABASE_URL = tu_url_de_supabase
   JWT_SECRET = tu_clave_jwt_aqui
   ENVIRONMENT = production
   NODE_ENV = production
   ```
6. Deploy

### 3️⃣ Variables de Entorno Necesarias

| Variable | Valor | Ejemplo |
|----------|-------|---------|
| `DATABASE_URL` | URL de conexión Supabase | `postgresql://user:pass@...` |
| `JWT_SECRET` | Clave secreta JWT (32+ chars) | Genera con `openssl rand -hex 32` |
| `ENVIRONMENT` | Ambiente de ejecución | `production` |
| `NODE_ENV` | Entorno de Node | `production` |

### 4️⃣ Cómo Funciona el Despliegue Unificado

```
┌─────────────────────────────────────────────────────┐
│         Render Web Service (Único)                  │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │  Express Server Proxy (Puerto 3000+)         │  │
│  │  - Sirve frontend compilado                  │  │
│  │  - Proxy: /api/* → Backend (localhost:8000)  │  │
│  └──────────────────────────────────────────────┘  │
│                      ↓                              │
│  ┌──────────────────────────────────────────────┐  │
│  │  FastAPI Backend (Puerto 8000, interno)      │  │
│  │  - APIs REST                                 │  │
│  │  - Conexión a Supabase                       │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Flujo de Requests:**
1. Usuario accede a `https://melius.onrender.com`
2. Express sirve el frontend compilado
3. Frontend hace request a `/api/usuarios`
4. Express proxy redirecciona a `http://localhost:8000/usuarios`
5. FastAPI procesa y responde
6. Express devuelve la respuesta al frontend

### 5️⃣ URL Final

Una vez desplegado:
- **Frontend + Backend:** `https://melius.onrender.com`
- **API Directa:** `https://melius.onrender.com/api/*`
- **Health Check:** `https://melius.onrender.com/health`

---

## 🐛 Troubleshooting

### El frontend se carga pero no conecta con el API
**Solución:**
1. Abre DevTools (F12) → Network
2. Verifica que las requests a `/api` reciben respuesta del backend
3. Revisa los logs en Render Dashboard → Logs

### Error "Backend unavailable"
**Causas y soluciones:**
1. Backend no inició correctamente
   - Verifica `DATABASE_URL` en variables de entorno
   - Revisa logs para errores de conexión a Supabase
2. Puerto 8000 en conflicto
   - El script debería manejar esto automáticamente

### Build fails con errores de Python
**Solución:**
```bash
# Verifica localmente
cd melius-backend
pip install -r requirements.txt
```

### Build fails con errores de Node/npm
**Solución:**
```bash
# Verifica localmente
cd Programa_Final_Frontend
npm install
npm run build
```

### Cambiar la URL del backend en el frontend (caso especial)
El frontend está configurado para usar `/api` como base. Si necesitas cambiar esto:

1. Edita `Programa_Final_Frontend/server-proxy.js`
2. Modifica la ruta del proxy (línea ~16)
3. Commit y push
4. Render se redeploya automáticamente

---

## 📱 Monitoreo en Producción

### Ver Logs
1. Dashboard → Melius → Logs
2. Filtra por "error" o "warning"

### Reiniciar Servicio
1. Dashboard → Melius → Manual Deploy → Deploy latest commit

### Ver Métricas
1. Dashboard → Melius → Metrics
2. CPU, RAM, requests, respuesta time

---

## 💡 Tips Importantes

✅ **CORS está configurado automáticamente** - El backend lee `FRONTEND_URL` aunque en despliegue unificado no la usa  
✅ **Proxy automático** - No necesitas cambiar nada en el frontend para que funcione  
✅ **Graceful shutdown** - El servidor maneja SIGTERM correctamente  
✅ **Health check disponible** - `/health` devuelve estado del servicio  
✅ **Base de datos** - Asegúrate que tu IP de Render esté whitelisted en Supabase  

---

## 🔄 Actualizaciones Futuras

Para hacer cambios:
1. Edita código en `melius-backend/` o `Programa_Final_Frontend/`
2. Commit y push a `version-despliegue`
3. Render se redeploya automáticamente

Para cambios en variables de entorno:
1. Dashboard → Melius → Environment → Edita variables
2. Haz click en "Save" y se reinicia el servicio

---

**Creado para el proyecto Melius S.A.C - Despliegue Unificado**

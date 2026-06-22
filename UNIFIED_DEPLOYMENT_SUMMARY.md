# 🔄 Cambios de Despliegue Unificado en Render

## ✅ Archivos Modificados

### Backend
- **`melius-backend/main.py`** - CORS dinámico configurado
- **`melius-backend/requirements.txt`** - Agregadas dependencias para producción

### Frontend
- **`Programa_Final_Frontend/package.json`** 
  - Agregada dependencia `http-proxy-middleware`
  - Script `start` actualizado para usar `proxy.conf.json`
- **`Programa_Final_Frontend/src/app/services/base-http.service.ts`**
  - Cambiado `API_BASE` de `http://localhost:8000` a `/api` (ruta relativa)
- **`Programa_Final_Frontend/proxy.conf.json`** (nuevo)
  - Configuración para proxy en desarrollo local

### Raíz del Proyecto
- **`render.yaml`** - Configuración para un único web service unificado
- **`start-unified.sh`** (nuevo) - Script que inicia backend + frontend
- **`Programa_Final_Frontend/server-proxy.js`** (nuevo) - Servidor Express que hace proxy
- **`.env.example`** - Plantilla de variables de entorno
- **`RENDER_DEPLOYMENT.md`** - Documentación de despliegue actualizada

---

## 🎯 Cómo Funciona

### Desarrollo Local
```bash
# Terminal 1: Backend
cd melius-backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Frontend
cd Programa_Final_Frontend
npm install
npm start  # ng serve --proxy-config proxy.conf.json
```

**Acceso:**
- Frontend: http://localhost:4200
- Backend API directo: http://localhost:8000
- API a través del proxy: http://localhost:4200/api/...

### Producción (Render)
- Render ejecuta `bash ./start-unified.sh`
- Script inicia backend en puerto 8000 (background)
- Script inicia frontend/proxy en puerto 3000+ (principal)
- Express proxy redirige `/api/*` → `localhost:8000/*`

**Acceso:**
- Todo en: https://melius.onrender.com

---

## 📝 Cambios en la Configuración de API

El frontend ahora usa rutas relativas:
```typescript
// Antes
const API_BASE = 'http://localhost:8000';

// Ahora
const API_BASE = '/api';
```

**Ventaja:** Funciona tanto en desarrollo (con proxy.conf.json) como en producción (con Express proxy)

---

## ✨ Resultado Final

✅ **Un único Web Service en Render**  
✅ **Frontend y Backend integrados**  
✅ **Mismo dominio (sin problemas CORS)**  
✅ **Funciona en desarrollo y producción**  
✅ **Fácil de mantener y actualizar**  

---

## 🚀 Próximo Paso

Hacer commit y push:
```bash
git add .
git commit -m "Configuración de despliegue unificado: un web service con backend + frontend"
git push origin version-despliegue
```

Luego despliega en Render usando `render.yaml`

# 🔐 Variables de Entorno para Render

## Dónde Obtener Cada Variable

### 1. SUPABASE_URL ✅
**Ya tienes:** `https://thvijujtbucrqtvvlvue.supabase.co`

---

### 2. SUPABASE_KEY ⚠️
**Necesitas obtenerlo de Supabase**

**Pasos:**
1. Ve a https://app.supabase.com
2. Abre tu proyecto "melius-sac"
3. En el menú lateral → **Settings** → **API**
4. Busca la sección **"Project API keys"**
5. Copia **"anon public"** (la primera de las dos claves)
6. Usa esa como `SUPABASE_KEY` en Render

⚠️ **IMPORTANTE:** Usa la clave **"anon"** (pública), NO la "service_role"

---

### 3. JWT_SECRET ✅
**Ya tienes:** `melius-sac-secret-key-2024`

---

## Variables en Render Dashboard

**En tu servicio "melius", ve a Environment:**

```
SUPABASE_URL = https://thvijujtbucrqtvvlvue.supabase.co
SUPABASE_KEY = <tu_anon_public_key_aqui>
JWT_SECRET = melius-sac-secret-key-2024
ENVIRONMENT = production
NODE_ENV = production
```

---

## Verificación Final

Después de agregar las variables:
1. Render automáticamente va a redeploy
2. Verifica los **Logs** por errores
3. Busca: "Backend ready" y "Frontend+proxy running"
4. Si todo está bien, tu URL será: `https://melius.onrender.com`

---

## ✅ Checklist

- [ ] Obtuviste SUPABASE_KEY de Supabase
- [ ] Agregaste todas las 5 variables en Render Environment
- [ ] Esperaste a que Render redeploy automáticamente
- [ ] Revisaste los logs por errores
- [ ] Accediste a https://melius.onrender.com (o tu URL)

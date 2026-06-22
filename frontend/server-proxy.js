/**
 * Servidor unificado que sirve el frontend y hace proxy del backend
 */
const express = require('express');
const http = require('http');
const { createProxyMiddleware } = require('http-proxy-middleware');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Proxy de todas las solicitudes a /api al backend
app.use(
  '/api',
  createProxyMiddleware({
    target: 'http://localhost:8000',
    changeOrigin: true,
    pathRewrite: {
      '^/api': '',
    },
    onError: (err, req, res) => {
      console.error('Proxy error:', err);
      res.status(503).json({ error: 'Backend unavailable' });
    },
  })
);

// Servir archivos estáticos del frontend compilado
const distPath = path.join(__dirname, 'dist/frontend/browser');
app.use(express.static(distPath));

// Para SSR (Server-Side Rendering)
// Importar el servidor de Angular compilado
const { renderApplication, renderPage } = require('@angular/platform-server');

// Health check
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'ok', service: 'melius-unified' });
});

// Rutas del API que existan en el frontend
app.use((req, res, next) => {
  // Si no es /api y no es un archivo estático, intenta SSR
  if (!req.path.startsWith('/api') && !req.path.includes('.')) {
    // Aquí iría la lógica de SSR si está habilitado
    // Por ahora, solo sirve el índice
    res.sendFile(path.join(distPath, 'index.html'));
  } else {
    next();
  }
});

// Captura todas las demás rutas y sirve index.html (SPA)
app.get('*', (req, res) => {
  res.sendFile(path.join(distPath, 'index.html'));
});

// Manejo de errores
app.use((err, req, res, next) => {
  console.error('Error:', err);
  res.status(500).json({ error: 'Internal server error' });
});

// Iniciar servidor
const server = http.createServer(app);
server.listen(PORT, '0.0.0.0', () => {
  console.log(`✅ Melius Unified Server running on port ${PORT}`);
  console.log(`📍 Frontend: http://0.0.0.0:${PORT}`);
  console.log(`📍 API Proxy: http://0.0.0.0:${PORT}/api`);
  console.log(`📍 Backend: http://localhost:8000`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received, closing server...');
  server.close(() => {
    console.log('Server closed');
    process.exit(0);
  });
});

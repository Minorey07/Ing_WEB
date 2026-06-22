#!/bin/bash

# Iniciar el backend FastAPI en puerto 8000 (background)
echo "🚀 Starting backend..."
cd melius-backend
uvicorn main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
cd ..

# Esperar a que el backend esté listo
sleep 2

# Iniciar el servidor proxy/frontend en el puerto principal
echo "🚀 Starting unified frontend+proxy server..."
cd Programa_Final_Frontend
node server-proxy.js

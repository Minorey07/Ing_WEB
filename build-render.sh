#!/bin/bash
set -e

echo "🔨 Build Stage 1: Installing backend dependencies..."
cd melius-backend
pip install -r requirements.txt
cd ..

echo "🔨 Build Stage 2: Building frontend..."
cd Programa_Final_Frontend
npm install
npm run build
cd ..

echo "✅ Build completed successfully!"

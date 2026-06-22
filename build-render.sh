#!/bin/bash
set -e

echo "🔨 Build Stage 1: Installing backend dependencies..."
cd backend
pip install -r requirements.txt
cd ..

echo "🔨 Build Stage 2: Building frontend..."
cd frontend
npm install
npm run build
cd ..

echo "✅ Build completed successfully!"

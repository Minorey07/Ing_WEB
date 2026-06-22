#!/bin/bash

echo "Building Melius Backend and Frontend..."

# Build Backend
echo "Installing backend dependencies..."
cd melius-backend
pip install -r requirements.txt
cd ..

# Build Frontend
echo "Building frontend..."
cd Programa_Final_Frontend
npm install --prefer-offline --no-audit
npm run build
cd ..

echo "Build completed!"

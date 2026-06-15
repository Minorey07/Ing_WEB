#!/usr/bin/env python3
"""
Script de verificación de normalización
Comprueba que todos los archivos necesarios están en su lugar
"""

import os
from pathlib import Path

def verificar_estructura():
    """Verifica que la estructura de archivos es correcta"""
    
    backend_path = Path(__file__).parent
    
    print("\n" + "="*70)
    print("✅ VERIFICACIÓN DE ESTRUCTURA NORMALIZACIÓN 3FN")
    print("="*70 + "\n")
    
    # Directorios a verificar
    dirs_esperados = {
        "repositorio": [
            "categoria_repository.py",
            "estado_producto_repository.py",
            "estado_pedido_repository.py",
            "rol_repository.py",
            "ubicacion_local_repository.py",
            "ubicacion_nacional_repository.py",
            "proveedor_repository.py",
            "serializador.py"
        ],
        "servicios": [
            "categoria_service.py",
            "estado_producto_service.py",
            "estado_pedido_service.py",
            "rol_service.py",
            "ubicacion_local_service.py",
            "ubicacion_nacional_service.py",
            "proveedor_service.py",
            "producto_service.py",  # Actualizado
            "usuario_service.py",   # Actualizado
            "cliente_service.py",   # Actualizado
            "pedido_service.py"     # Actualizado
        ],
        "apis": [
            "categoria_api.py",
            "estado_producto_api.py",
            "estado_pedido_api.py",
            "rol_api.py",
            "ubicacion_local_api.py",
            "ubicacion_nacional_api.py",
            "system_api.py"
        ]
    }
    
    archivos_esperados = [
        "inicializacion.py",
        "main.py",  # Actualizado
        "NORMALIZACION_CAMBIOS.md"
    ]
    
    # Verificar directorios
    archivos_encontrados = 0
    archivos_faltantes = 0
    
    for directorio, archivos in dirs_esperados.items():
        dir_path = backend_path / directorio
        print(f"\n📁 Directorio: {directorio}/")
        print("-" * 70)
        
        for archivo in archivos:
            file_path = dir_path / archivo
            if file_path.exists():
                size = file_path.stat().st_size
                print(f"  ✅ {archivo:<40} ({size:,} bytes)")
                archivos_encontrados += 1
            else:
                print(f"  ❌ {archivo:<40} (NO ENCONTRADO)")
                archivos_faltantes += 1
    
    # Verificar archivos raíz
    print(f"\n📁 Raíz del backend/")
    print("-" * 70)
    
    for archivo in archivos_esperados:
        file_path = backend_path / archivo
        if file_path.exists():
            size = file_path.stat().st_size
            print(f"  ✅ {archivo:<40} ({size:,} bytes)")
            archivos_encontrados += 1
        else:
            print(f"  ❌ {archivo:<40} (NO ENCONTRADO)")
            archivos_faltantes += 1
    
    # Resumen
    print("\n" + "="*70)
    print(f"📊 RESUMEN")
    print("="*70)
    print(f"✅ Archivos encontrados:  {archivos_encontrados}")
    print(f"❌ Archivos faltantes:    {archivos_faltantes}")
    
    if archivos_faltantes == 0:
        print("\n🎉 ¡ESTRUCTURA COMPLETA Y CORRECTA!")
        print("\n📋 Próximos pasos:")
        print("  1. Instalar FastAPI si no está instalado:")
        print("     pip install fastapi uvicorn")
        print("  2. Arrancar el servidor:")
        print("     python -m uvicorn main:app --reload")
        print("  3. Acceder a:")
        print("     http://localhost:8000/status")
        print("     http://localhost:8000/inicializar")
        return True
    else:
        print("\n⚠️  FALTAN ARCHIVOS")
        print("Por favor, verifica la instalación.")
        return False


if __name__ == "__main__":
    exito = verificar_estructura()
    exit(0 if exito else 1)

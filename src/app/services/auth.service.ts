import { Injectable } from '@angular/core';
import { Usuario } from '../models/usuario.model';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private usuarioActual: Usuario | null = null;

  // 🔥 usuarios simulados (luego esto va a base de datos)
  private usuarios: Usuario[] = [
    {
      nombre: 'Administrador',
      correo: 'admin@melius.com',
      password: '123',
      rol: 'ADMIN'
    },
    {
      nombre: 'Almacenero',
      correo: 'almacen@melius.com',
      password: '123',
      rol: 'ALMACENERO'
    },
    {
      nombre: 'Vendedor',
      correo: 'vendedor@melius.com',
      password: '123',
      rol: 'VENDEDOR'
    }
  ];

  login(correo: string, password: string): boolean {

    const user = this.usuarios.find(
      u => u.correo === correo && u.password === password
    );

    if (!user) return false;

    this.usuarioActual = user;
    localStorage.setItem('usuario', JSON.stringify(user));

    return true;
  }

  logout(): void {
    this.usuarioActual = null;
    localStorage.removeItem('usuario');
  }

  getUsuarioActual(): Usuario | null {

    if (this.usuarioActual) return this.usuarioActual;

    const data = localStorage.getItem('usuario');

    if (data) {
      this.usuarioActual = JSON.parse(data);
      return this.usuarioActual;
    }

    return null;
  }

  getRol(): string | undefined {
    return this.getUsuarioActual()?.rol;
  }

  isLoggedIn(): boolean {
    return this.getUsuarioActual() !== null;
  }
}
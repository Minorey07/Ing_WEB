import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';

export interface AuthUser {
  id: number;
  nombre: string;
  correo: string;
  rol: 'ADMIN' | 'ALMACENERO' | 'VENDEDOR';
  rolId?: number;
}

export interface LoginResponse {
  token: string;
  usuario: AuthUser;
}

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private usuarioActual: AuthUser | null = null;

  constructor(private http: BaseHttpService) {}

  async login(correo: string, password: string): Promise<boolean> {
    try {
      const resp = await this.http.post<LoginResponse>('/auth/login', { correo, password });
      this.usuarioActual = resp.usuario;
      localStorage.setItem(
        'usuario',
        JSON.stringify({ ...resp.usuario, token: resp.token })
      );
      return true;
    } catch {
      return false;
    }
  }

  logout(): void {
    this.usuarioActual = null;
    localStorage.removeItem('usuario');
  }

  getUsuarioActual(): AuthUser | null {
    if (this.usuarioActual) return this.usuarioActual;
    const data = localStorage.getItem('usuario');
    if (data) {
      try {
        const parsed = JSON.parse(data);
        this.usuarioActual = parsed;
        return parsed;
      } catch {
        return null;
      }
    }
    return null;
  }

  getRol(): string | undefined {
    return this.getUsuarioActual()?.rol;
  }

  isLoggedIn(): boolean {
    return this.getUsuarioActual() !== null;
  }

  getToken(): string | null {
    const data = localStorage.getItem('usuario');
    if (!data) return null;
    try {
      return JSON.parse(data).token || null;
    } catch {
      return null;
    }
  }
}

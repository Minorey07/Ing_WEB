import { Injectable } from '@angular/core';
import { BaseHttpService } from './base-http.service';
import { Usuario } from '../models/usuario.model';

@Injectable({ providedIn: 'root' })
export class UsuarioService {
  constructor(private http: BaseHttpService) {}

  listar(): Promise<Usuario[]> {
    return this.http.get<Usuario[]>('/usuarios/');
  }

  crear(usuario: Usuario): Promise<Usuario> {
    return this.http.post<Usuario>('/usuarios/', usuario);
  }

  actualizar(usuario: Usuario): Promise<Usuario> {
    return this.http.put<Usuario>(`/usuarios/${usuario.id}`, usuario);
  }

  eliminar(id: number): Promise<void> {
    return this.http.delete<void>(`/usuarios/${id}`);
  }
}

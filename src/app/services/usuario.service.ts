import { Injectable } from '@angular/core';
import { Usuario } from '../models/usuario.model';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  private usuarios: Usuario[] = [];

  private contadorId = 1;

  guardarUsuario(usuario: Usuario) {

    usuario.id = this.contadorId.toString();

    this.contadorId++;

    this.usuarios.push(usuario);

  }

  mostrarUsuarios(): Usuario[] {

    return this.usuarios;

  }

  eliminarUsuario(id: string) {

    this.usuarios =
      this.usuarios.filter(
        usuario => usuario.id !== id
      );

  }

  actualizarUsuario(usuarioActualizado: Usuario) {

    const indice =
      this.usuarios.findIndex(
        usuario => usuario.id === usuarioActualizado.id
      );

    if (indice !== -1) {

      this.usuarios[indice] =
        usuarioActualizado;

    }

  }

}
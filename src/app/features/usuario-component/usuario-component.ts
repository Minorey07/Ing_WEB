import { Component, inject, signal } from '@angular/core';

import { FormField } from '@angular/forms/signals';
import { form, required } from '@angular/forms/signals';

import { Usuario } from '../../models/usuario.model';
import { UsuarioService } from '../../services/usuario.service';

@Component({
  selector: 'app-usuario-component',
  imports: [FormField],
  templateUrl: './usuario-component.html',
  styleUrl: './usuario-component.css',
})
export class UsuarioComponent {

  usuarioService = inject(UsuarioService);

  listaUsuarios: Usuario[] = [];

  modoEdicion = false;

  idEditando = '';

  constructor() {

    this.mostrarUsuarios();

  }

  modeloUsuario = signal<Usuario>({
    nombre: '',
    correo: '',
    password: '',
    rol: 'VENDEDOR'
  });

  formularioUsuario = form(this.modeloUsuario, (esquema) => {

    required(esquema.nombre);

    required(esquema.correo);

    required(esquema.password);

    required(esquema.rol);

  });

  guardar(event: Event) {

    event.preventDefault();

    let usuario: Usuario = {

      id: this.idEditando,

      nombre:
        this.formularioUsuario.nombre().value(),

      correo:
        this.formularioUsuario.correo().value(),

      password:
        this.formularioUsuario.password().value(),

      rol:
        this.formularioUsuario.rol().value()

    };

    if (this.modoEdicion) {

      this.usuarioService.actualizarUsuario(usuario);

      this.modoEdicion = false;

      this.idEditando = '';

    } else {

      this.usuarioService.guardarUsuario(usuario);

    }

    this.mostrarUsuarios();

    this.limpiarFormulario();

  }

  mostrarUsuarios() {

    this.listaUsuarios =
      this.usuarioService.mostrarUsuarios();

  }

  editar(usuario: Usuario) {

    this.modoEdicion = true;

    this.idEditando = usuario.id!;

    this.formularioUsuario.nombre()
      .value.set(usuario.nombre);

    this.formularioUsuario.correo()
      .value.set(usuario.correo);

    this.formularioUsuario.password()
      .value.set(usuario.password);

    this.formularioUsuario.rol()
      .value.set(usuario.rol);

  }

  eliminar(id: string) {

    this.usuarioService.eliminarUsuario(id);

    this.mostrarUsuarios();

  }

  limpiarFormulario() {

    this.formularioUsuario.nombre()
      .value.set('');

    this.formularioUsuario.correo()
      .value.set('');

    this.formularioUsuario.password()
      .value.set('');

    this.formularioUsuario.rol()
      .value.set('VENDEDOR');

  }

}
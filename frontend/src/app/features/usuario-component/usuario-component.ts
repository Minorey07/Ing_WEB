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
  listaUsuarios = signal<Usuario[]>([]);
  modoEdicion = false;
  idEditando = 0;

  constructor() {
    this.cargarUsuarios();
  }

  async cargarUsuarios() {
    this.listaUsuarios.set(await this.usuarioService.listar());
  }

  modeloUsuario = signal<Usuario>({ nombre: '', correo: '', password: '', rolId: 3, rolNombre: '' });

  formularioUsuario = form(this.modeloUsuario, (esquema) => {
    required(esquema.nombre);
    required(esquema.correo);
    required(esquema.password);
  });

  get rolIdValue(): number {
    return this.modeloUsuario().rolId;
  }

  actualizarRol(event: Event) {
    const value = Number((event.target as HTMLSelectElement).value);
    this.modeloUsuario.set({ ...this.modeloUsuario(), rolId: value });
  }

  async guardar(event: Event) {
    event.preventDefault();
    let usuario: Usuario = {
      id: this.idEditando || undefined,
      nombre: this.formularioUsuario.nombre().value(),
      correo: this.formularioUsuario.correo().value(),
      password: this.formularioUsuario.password().value(),
      rolId: this.modeloUsuario().rolId
    };
    if (this.modoEdicion) {
      await this.usuarioService.actualizar(usuario);
      this.modoEdicion = false;
      this.idEditando = 0;
    } else {
      await this.usuarioService.crear(usuario);
    }
    await this.cargarUsuarios();
    this.limpiarFormulario();
  }

  editar(usuario: Usuario) {
    this.modoEdicion = true;
    this.idEditando = usuario.id!;
    this.formularioUsuario.nombre().value.set(usuario.nombre);
    this.formularioUsuario.correo().value.set(usuario.correo);
    this.formularioUsuario.password().value.set(usuario.password);
    this.modeloUsuario.set({ ...this.modeloUsuario(), rolId: usuario.rolId });
  }

  async eliminar(id: number) {
    await this.usuarioService.eliminar(id);
    await this.cargarUsuarios();
  }

  limpiarFormulario() {
    this.formularioUsuario.nombre().value.set('');
    this.formularioUsuario.correo().value.set('');
    this.formularioUsuario.password().value.set('');
    this.modeloUsuario.set({ ...this.modeloUsuario(), rolId: 3 });
  }
}

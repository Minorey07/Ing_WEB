import { Component, inject, signal } from '@angular/core';

import { FormField } from '@angular/forms/signals';
import { form, required } from '@angular/forms/signals';

import { Cliente } from '../../models/cliente.model';
import { ClienteService } from '../../services/cliente.service';

@Component({
  selector: 'app-cliente-component',
  imports: [FormField],
  templateUrl: './cliente-component.html',
  styleUrl: './cliente-component.css',
})
export class ClienteComponent {

  clienteService = inject(ClienteService);

  listaClientes: Cliente[] = [];

  modoEdicion = false;

  idEditando = 0;

  constructor() {

    this.mostrarClientes();

  }

  modeloCliente = signal<Cliente>({
    id: 0,
    nombres: '',
    telefono: '',
    direccion: ''
  });

  formularioCliente = form(this.modeloCliente, (esquema) => {

    required(esquema.nombres, {
      message: 'El nombre es obligatorio'
    });

    required(esquema.telefono, {
      message: 'El teléfono es obligatorio'
    });

    required(esquema.direccion, {
      message: 'La dirección es obligatoria'
    });

  });

  guardar(event: Event) {

    event.preventDefault();

    let cliente: Cliente = {

      id: this.idEditando,

      nombres:
        this.formularioCliente.nombres().value(),

      telefono:
        this.formularioCliente.telefono().value(),

      direccion:
        this.formularioCliente.direccion().value()

    };

    if (this.modoEdicion) {

      this.clienteService.actualizarCliente(
        cliente
      );

      this.modoEdicion = false;

      this.idEditando = 0;

    } else {

      this.clienteService.guardarCliente(
        cliente
      );

    }

    this.mostrarClientes();

    this.limpiarFormulario();

  }

  mostrarClientes() {

    this.listaClientes =
      this.clienteService.mostrarClientes();

  }

  editar(cliente: Cliente) {

    this.modoEdicion = true;

    this.idEditando = cliente.id;

    this.formularioCliente.nombres()
      .value.set(cliente.nombres);

    this.formularioCliente.telefono()
      .value.set(cliente.telefono);

    this.formularioCliente.direccion()
      .value.set(cliente.direccion);

  }

  eliminar(id: number) {

    this.clienteService.eliminarCliente(id);

    this.mostrarClientes();

  }

  limpiarFormulario() {

    this.formularioCliente.nombres()
      .value.set('');

    this.formularioCliente.telefono()
      .value.set('');

    this.formularioCliente.direccion()
      .value.set('');

  }

  get totalClientes(): number {

  return this.listaClientes.length;

}

}

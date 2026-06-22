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
  listaClientes = signal<Cliente[]>([]);
  modoEdicion = false;
  idEditando = 0;

  constructor() {
    this.cargarClientes();
  }

  async cargarClientes() {
    this.listaClientes.set(await this.clienteService.listar());
  }

  modeloCliente = signal<Cliente>({
    id: 0, nombres: '', telefono: '', direccion: ''
  });

  formularioCliente = form(this.modeloCliente, (esquema) => {
    required(esquema.nombres, { message: 'El nombre es obligatorio' });
    required(esquema.telefono, { message: 'El teléfono es obligatorio' });
    required(esquema.direccion, { message: 'La dirección es obligatoria' });
  });

  async guardar(event: Event) {
    event.preventDefault();
    let cliente: Cliente = {
      id: this.idEditando,
      nombres: this.formularioCliente.nombres().value(),
      telefono: this.formularioCliente.telefono().value(),
      direccion: this.formularioCliente.direccion().value()
    };
    if (this.modoEdicion) {
      await this.clienteService.actualizar(cliente);
      this.modoEdicion = false;
      this.idEditando = 0;
    } else {
      await this.clienteService.crear(cliente);
    }
    await this.cargarClientes();
    this.limpiarFormulario();
  }

  editar(cliente: Cliente) {
    this.modoEdicion = true;
    this.idEditando = cliente.id;
    this.formularioCliente.nombres().value.set(cliente.nombres);
    this.formularioCliente.telefono().value.set(cliente.telefono);
    this.formularioCliente.direccion().value.set(cliente.direccion);
  }

  async eliminar(id: number) {
    await this.clienteService.eliminar(id);
    await this.cargarClientes();
  }

  limpiarFormulario() {
    this.formularioCliente.nombres().value.set('');
    this.formularioCliente.telefono().value.set('');
    this.formularioCliente.direccion().value.set('');
  }

  get totalClientes(): number {
    return this.listaClientes().length;
  }
}

import { Component, inject, signal } from '@angular/core';
import { FormField } from '@angular/forms/signals';
import { form, required } from '@angular/forms/signals';
import { Proveedor } from '../../models/proveedor.model';
import { ProveedorService } from '../../services/proveedor.service';

@Component({
  selector: 'app-proveedor-component',
  imports: [FormField],
  templateUrl: './proveedor-component.html',
  styleUrl: './proveedor-component.css',
})
export class ProveedorComponent {
  proveedorService = inject(ProveedorService);
  listaProveedores = signal<Proveedor[]>([]);
  modoEdicion = false;
  idEditando = 0;

  constructor() {
    this.cargarProveedores();
  }

  async cargarProveedores() {
    this.listaProveedores.set(await this.proveedorService.listar());
  }

  modeloProveedor = signal<Proveedor>({
    id: 0, razonSocial: '', ruc: '', telefono: '', direccion: ''
  });

  formularioProveedor = form(this.modeloProveedor, (esquema) => {
    required(esquema.razonSocial, { message: 'La razón social es obligatoria' });
    required(esquema.ruc, { message: 'El RUC es obligatorio' });
    required(esquema.telefono, { message: 'El teléfono es obligatorio' });
    required(esquema.direccion, { message: 'La dirección es obligatoria' });
  });

  async guardar(event: Event) {
    event.preventDefault();
    let proveedor: Proveedor = {
      id: this.idEditando,
      razonSocial: this.formularioProveedor.razonSocial().value(),
      ruc: this.formularioProveedor.ruc().value(),
      telefono: this.formularioProveedor.telefono().value(),
      direccion: this.formularioProveedor.direccion().value()
    };
    if (this.modoEdicion) {
      await this.proveedorService.actualizar(proveedor);
      this.modoEdicion = false;
      this.idEditando = 0;
    } else {
      await this.proveedorService.crear(proveedor);
    }
    await this.cargarProveedores();
    this.limpiarFormulario();
  }

  editar(proveedor: Proveedor) {
    this.modoEdicion = true;
    this.idEditando = proveedor.id;
    this.formularioProveedor.razonSocial().value.set(proveedor.razonSocial);
    this.formularioProveedor.ruc().value.set(proveedor.ruc);
    this.formularioProveedor.telefono().value.set(proveedor.telefono);
    this.formularioProveedor.direccion().value.set(proveedor.direccion);
  }

  async eliminar(id: number) {
    await this.proveedorService.eliminar(id);
    await this.cargarProveedores();
  }

  limpiarFormulario() {
    this.formularioProveedor.razonSocial().value.set('');
    this.formularioProveedor.ruc().value.set('');
    this.formularioProveedor.telefono().value.set('');
    this.formularioProveedor.direccion().value.set('');
  }

  get totalProveedores(): number {
    return this.listaProveedores.length;
  }
}

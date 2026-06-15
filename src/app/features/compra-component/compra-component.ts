import { Component, inject, signal } from '@angular/core';

import { FormField } from '@angular/forms/signals';
import { form, required } from '@angular/forms/signals';

import { Compra } from '../../models/compra.model';
import { CompraService } from '../../services/compra.service';

@Component({
  selector: 'app-compra-component',
  imports: [FormField],
  templateUrl: './compra-component.html',
  styleUrl: './compra-component.css',
})
export class CompraComponent {

  compraService = inject(CompraService);

  listaCompras: Compra[] = [];

  modoEdicion = false;

  idEditando = 0;

  constructor() {

    this.mostrarCompras();

  }

  modeloCompra = signal<Compra>({
    id: 0,
    proveedorId: 0,
    fecha: new Date(),
    total: 0
  });

  formularioCompra = form(this.modeloCompra, (esquema) => {

    required(esquema.proveedorId);

    required(esquema.total);

  });

  guardar(event: Event) {

    event.preventDefault();

    let compra: Compra = {

      id: this.idEditando,

      proveedorId:
        this.formularioCompra.proveedorId().value(),

      fecha: new Date(),

      total:
        this.formularioCompra.total().value()

    };

    if (this.modoEdicion) {

      this.compraService.actualizarCompra(compra);

      this.modoEdicion = false;

      this.idEditando = 0;

    } else {

      this.compraService.guardarCompra(compra);

    }

    this.mostrarCompras();

    this.limpiarFormulario();

  }

  mostrarCompras() {

    this.listaCompras =
      this.compraService.mostrarCompras();

  }

  editar(compra: Compra) {

    this.modoEdicion = true;

    this.idEditando = compra.id;

    this.formularioCompra.proveedorId()
      .value.set(compra.proveedorId);

    this.formularioCompra.total()
      .value.set(compra.total);

  }

  eliminar(id: number) {

    this.compraService.eliminarCompra(id);

    this.mostrarCompras();

  }

  limpiarFormulario() {

    this.formularioCompra.proveedorId()
      .value.set(0);

    this.formularioCompra.total()
      .value.set(0);

  }

  get totalCompras(): number {

  return this.listaCompras.reduce(
    (total, compra) => total + compra.total,
    0
  );

}

}
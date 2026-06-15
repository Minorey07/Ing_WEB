import { Component, inject, signal } from '@angular/core';
import { FormField } from '@angular/forms/signals';
import { form, required } from '@angular/forms/signals';

import { Producto } from '../../models/producto.model';
import { ProductoService } from '../../services/producto.service';

@Component({
  selector: 'app-producto-component',
  imports: [FormField],
  templateUrl: './producto-component.html',
  styleUrl: './producto-component.css',
})
export class ProductoComponent {

  productoService = inject(ProductoService);

  listaProductos: Producto[] = [];

  modoEdicion = false;

  idEditando = 0;

  constructor() {

    this.mostrarProductos();

  }

  modeloProducto = signal<Producto>({
    id: 0,
    nombre: '',
    descripcion: '',
    precio: 0,
    stock: 0,
    estado: ''
  });

  formularioProducto = form(this.modeloProducto, (esquema) => {

    required(esquema.nombre, {
      message: 'El nombre es obligatorio'
    });

    required(esquema.descripcion, {
      message: 'La descripción es obligatoria'
    });

    required(esquema.precio, {
      message: 'El precio es obligatorio'
    });

    required(esquema.stock, {
      message: 'El stock es obligatorio'
    });

  });

  guardar(event: Event) {

    event.preventDefault();

    let stock =
      this.formularioProducto.stock().value();

    let producto: Producto = {

      id: this.idEditando,

      nombre:
        this.formularioProducto.nombre().value(),

      descripcion:
        this.formularioProducto.descripcion().value(),

      precio:
        this.formularioProducto.precio().value(),

      stock: stock,

      estado:
        stock > 0 ? 'ACTIVO' : 'AGOTADO'

    };

    if (this.modoEdicion) {

      this.productoService.actualizarProducto(
        producto
      );

      this.modoEdicion = false;

      this.idEditando = 0;

    } else {

      this.productoService.guardarProducto(
        producto
      );

    }

    this.mostrarProductos();

    this.limpiarFormulario();

  }

  mostrarProductos() {

    this.listaProductos =
      this.productoService.mostrarProductos();

  }

  editar(producto: Producto) {

    this.modoEdicion = true;

    this.idEditando = producto.id;

    this.formularioProducto.nombre()
      .value.set(producto.nombre);

    this.formularioProducto.descripcion()
      .value.set(producto.descripcion);

    this.formularioProducto.precio()
      .value.set(producto.precio);

    this.formularioProducto.stock()
      .value.set(producto.stock);

  }

  eliminar(id: number) {

    this.productoService.eliminarProducto(id);

    this.mostrarProductos();

  }

  limpiarFormulario() {

    this.formularioProducto.nombre()
      .value.set('');

    this.formularioProducto.descripcion()
      .value.set('');

    this.formularioProducto.precio()
      .value.set(0);

    this.formularioProducto.stock()
      .value.set(0);

  }

  get stockTotal(): number {

    return this.listaProductos.reduce(
      (total, producto) => total + producto.stock,
      0
    );

  }

  get valorInventario(): number {

    return this.listaProductos.reduce(
      (total, producto) =>
        total + (producto.stock * producto.precio),
      0
    );

  }

  get ultimoProducto(): string {

    if (this.listaProductos.length === 0) {

      return 'Sin registros';

    }

    return this.listaProductos[
      this.listaProductos.length - 1
    ].nombre;

  }

}
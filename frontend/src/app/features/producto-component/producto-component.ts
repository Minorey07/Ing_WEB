import { Component, inject, signal } from '@angular/core';
import { FormField } from '@angular/forms/signals';
import { form, required } from '@angular/forms/signals';
import { Producto } from '../../models/producto.model';
import { Categoria } from '../../models/categoria.model';
import { ProductoService } from '../../services/producto.service';
import { AuthService } from '../../services/auth.service';
import { BaseHttpService } from '../../services/base-http.service';

@Component({
  selector: 'app-producto-component',
  imports: [FormField],
  templateUrl: './producto-component.html',
  styleUrl: './producto-component.css',
})
export class ProductoComponent {
  productoService = inject(ProductoService);
  authService = inject(AuthService);
  http = inject(BaseHttpService);

  listaProductos = signal<Producto[]>([]);
  listaCategorias = signal<Categoria[]>([]);
  modoEdicion = false;
  idEditando = 0;
  rolId = 0;

  constructor() {
    this.rolId = this.authService.getUsuarioActual()?.rolId ?? 0;
    this.cargarCategorias();
    this.cargarProductos();
  }

  async cargarProductos() {
    this.listaProductos.set(await this.productoService.listar());
  }

  async cargarCategorias() {
    try {
      this.listaCategorias.set(await this.http.get<Categoria[]>('/categorias/'));
    } catch {}
  }

  get esSoloLectura(): boolean {
    return this.rolId === 3;
  }

  modeloProducto = signal<Producto>({
    id: 0, nombre: '', descripcion: '', precio: 0, stock: 0, estadoId: 1, categoriaId: undefined
  });

  formularioProducto = form(this.modeloProducto, (esquema) => {
    required(esquema.nombre, { message: 'El nombre es obligatorio' });
    required(esquema.descripcion, { message: 'La descripción es obligatoria' });
    required(esquema.precio, { message: 'El precio es obligatorio' });
    required(esquema.stock, { message: 'El stock es obligatorio' });
  });

  async guardar(event: Event) {
    event.preventDefault();
    if (this.esSoloLectura) return;
    let producto: Producto = {
      id: this.idEditando,
      nombre: this.formularioProducto.nombre().value(),
      descripcion: this.formularioProducto.descripcion().value(),
      precio: this.formularioProducto.precio().value(),
      stock: this.formularioProducto.stock().value(),
      estadoId: this.modeloProducto().estadoId,
      categoriaId: this.modeloProducto().categoriaId
    };
    if (this.modoEdicion) {
      await this.productoService.actualizar(producto);
      this.modoEdicion = false;
      this.idEditando = 0;
    } else {
      await this.productoService.crear(producto);
    }
    await this.cargarProductos();
    this.limpiarFormulario();
  }

  async actualizarCategoria(event: Event) {
    const value = Number((event.target as HTMLSelectElement).value);
    this.modeloProducto.set({ ...this.modeloProducto(), categoriaId: value || undefined });
  }

  async actualizarEstado(event: Event) {
    const value = Number((event.target as HTMLSelectElement).value);
    this.modeloProducto.set({ ...this.modeloProducto(), estadoId: value });
  }

  editar(producto: Producto) {
    this.modoEdicion = true;
    this.idEditando = producto.id;
    this.formularioProducto.nombre().value.set(producto.nombre);
    this.formularioProducto.descripcion().value.set(producto.descripcion);
    this.formularioProducto.precio().value.set(producto.precio);
    this.formularioProducto.stock().value.set(producto.stock);
    this.modeloProducto.set({
      ...this.modeloProducto(),
      estadoId: producto.estadoId,
      categoriaId: producto.categoriaId
    });
  }

  async eliminar(id: number) {
    if (this.esSoloLectura) return;
    await this.productoService.eliminar(id);
    await this.cargarProductos();
  }

  limpiarFormulario() {
    this.formularioProducto.nombre().value.set('');
    this.formularioProducto.descripcion().value.set('');
    this.formularioProducto.precio().value.set(0);
    this.formularioProducto.stock().value.set(0);
    this.modeloProducto.set({ ...this.modeloProducto(), estadoId: 1, categoriaId: undefined });
  }

  get stockTotal(): number {
    return this.listaProductos().reduce((total, p) => total + p.stock, 0);
  }

  get valorInventario(): number {
    return this.listaProductos().reduce((t, p) => t + p.stock * p.precio, 0);
  }

  get ultimoProducto(): string {
    if (this.listaProductos().length === 0) return 'Sin registros';
    return this.listaProductos()[this.listaProductos().length - 1].nombre;
  }
}

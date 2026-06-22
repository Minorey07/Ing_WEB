import { Component, inject, signal } from '@angular/core';
import { Pedido } from '../../models/pedido.model';
import { Cliente } from '../../models/cliente.model';
import { Producto } from '../../models/producto.model';
import { PedidoDetalle } from '../../models/PedidoDetalle.model';
import { PedidoService } from '../../services/pedido.service';
import { ClienteService } from '../../services/cliente.service';
import { ProductoService } from '../../services/producto.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-pedido-component',
  templateUrl: './pedido-component.html',
  styleUrl: './pedido-component.css',
})
export class PedidoComponent {
  pedidoService = inject(PedidoService);
  clienteService = inject(ClienteService);
  productoService = inject(ProductoService);
  authService = inject(AuthService);

  listaPedidos = signal<Pedido[]>([]);
  listaClientes = signal<Cliente[]>([]);
  listaProductos = signal<Producto[]>([]);
  carrito: PedidoDetalle[] = [];
  modoEdicion = false;
  idEditando = 0;
  nombreVendedor = '';
  rolId = 0;

  constructor() {
    this.inicializar();
  }

  async inicializar() {
    this.listaClientes.set(await this.clienteService.listar());
    this.listaProductos.set(await this.productoService.listar());
    this.listaPedidos.set(await this.pedidoService.listar());
    const user = this.authService.getUsuarioActual();
    if (user) {
      this.nombreVendedor = user.nombre;
      this.rolId = user.rolId ?? 0;
    }
  }

  modeloPedido = signal<{ clienteId: number; estadoId: number }>({
    clienteId: 0,
    estadoId: 1
  });

  agregarProducto(producto: Producto) {
    const item = this.carrito.find(p => p.productoId === producto.id);
    const cantidadEnCarrito = item ? item.cantidad : 0;
    if (cantidadEnCarrito >= producto.stock) {
      alert('No hay más stock disponible');
      return;
    }
    if (item) {
      item.cantidad++;
      item.subtotal = item.cantidad * item.precio;
    } else {
      this.carrito.push({
        productoId: producto.id,
        nombre: producto.nombre,
        cantidad: 1,
        precio: producto.precio,
        subtotal: producto.precio
      });
    }
  }

  disminuir(producto: Producto) {
    const item = this.carrito.find(p => p.productoId === producto.id);
    if (!item) return;
    item.cantidad--;
    if (item.cantidad <= 0) {
      this.carrito = this.carrito.filter(p => p.productoId !== producto.id);
    } else {
      item.subtotal = item.cantidad * item.precio;
    }
  }

  get totalCalculado(): number {
    return this.carrito.reduce((t, i) => t + i.subtotal, 0);
  }

  actualizarCliente(event: Event) {
    const value = Number((event.target as HTMLSelectElement).value);
    this.modeloPedido.set({ ...this.modeloPedido(), clienteId: value });
  }

  actualizarEstado(event: Event) {
    const value = Number((event.target as HTMLSelectElement).value);
    this.modeloPedido.set({ ...this.modeloPedido(), estadoId: value });
  }

  async guardar(event: Event) {
    event.preventDefault();
    const user = this.authService.getUsuarioActual();
    const pedido: Pedido = {
      id: this.idEditando,
      clienteId: this.modeloPedido().clienteId,
      vendedorId: user?.id || 1,
      fecha: new Date(),
      estadoId: this.modeloPedido().estadoId,
      total: this.totalCalculado,
      detalles: [...this.carrito]
    };
    if (this.modoEdicion) {
      await this.pedidoService.actualizar(pedido);
    } else {
      await this.pedidoService.crear(pedido);
    }
    this.listaPedidos.set(await this.pedidoService.listar());
    this.limpiar();
  }

  async editar(p: Pedido) {
    this.modoEdicion = true;
    this.idEditando = p.id;
    this.modeloPedido.set({ clienteId: p.clienteId, estadoId: p.estadoId });
    this.carrito = p.detalles.map(d => ({
      ...d,
      nombre: d.productoNombre || d.nombre || this.getNombreProducto(d.productoId)
    }));
  }

  async eliminar(id: number) {
    await this.pedidoService.eliminar(id);
    this.listaPedidos.set(await this.pedidoService.listar());
  }

  limpiar() {
    this.modeloPedido.set({ clienteId: 0, estadoId: 1 });
    this.carrito = [];
  }

  get pedidosPendientes() {
    return this.listaPedidos().filter(p => p.estadoId === 1).length;
  }

  get pedidosEntregados() {
    return this.listaPedidos().filter(p => p.estadoId === 2).length;
  }

  get totalVentas() {
    return this.listaPedidos().reduce((t, p) => t + p.total, 0);
  }

  getNombreProducto(id: number): string {
    const producto = this.listaProductos().find(p => p.id === id);
    return producto ? producto.nombre : 'Producto #' + id;
  }

  getNombreCliente(id: number): string {
    const cliente = this.listaClientes().find(c => c.id === id);
    return cliente ? cliente.nombres : 'Desconocido';
  }

  getNombreVendedor(): string {
    const user = this.authService.getUsuarioActual();
    return user ? user.nombre : 'Sistema';
  }
}

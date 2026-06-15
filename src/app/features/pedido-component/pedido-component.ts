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

  listaPedidos: Pedido[] = [];
  listaClientes: Cliente[] = [];
  listaProductos: Producto[] = [];

  carrito: PedidoDetalle[] = [];

  modoEdicion = false;
  idEditando = 0;

  nombreVendedor = '';

  constructor() {
    this.mostrarPedidos();
    this.listaClientes = this.clienteService.mostrarClientes();
    this.listaProductos = this.productoService.mostrarProductos();

    const user = this.authService.getUsuarioActual();
    if (user) this.nombreVendedor = user.nombre;
  }

  // ✅ FIX IMPORTANTE: estado bien tipado
  modeloPedido = signal<{
    clienteId: string;
    estado: 'PENDIENTE' | 'ENTREGADO';
  }>({
    clienteId: '',
    estado: 'PENDIENTE'
  });

  // 🟢 AGREGAR PRODUCTO (CON STOCK)
  agregarProducto(producto: Producto) {

    const item = this.carrito.find(p => p.productoId === producto.id);

    // 🔥 VALIDAR STOCK
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

  // ➖ DISMINUIR
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

  // 💰 TOTAL
  get totalCalculado(): number {
    return this.carrito.reduce((t, i) => t + i.subtotal, 0);
  }

  // 🧠 CLIENTE
  actualizarCliente(event: Event) {
    const value = (event.target as HTMLSelectElement).value;

    this.modeloPedido.set({
      ...this.modeloPedido(),
      clienteId: value
    });
  }

  // 🧠 ESTADO
  actualizarEstado(event: Event) {
    const value = (event.target as HTMLSelectElement).value;

    this.modeloPedido.set({
      ...this.modeloPedido(),
      estado: value as 'PENDIENTE' | 'ENTREGADO'
    });
  }

  // 💾 GUARDAR
  guardar(event: Event) {
    event.preventDefault();

    const pedido: Pedido = {
      id: this.idEditando,
      clienteId: Number(this.modeloPedido().clienteId),
      vendedorId: 1,
      fecha: new Date(),
      estado: this.modeloPedido().estado,
      total: this.totalCalculado,
      detalles: [...this.carrito]
    };

    if (this.modoEdicion) {
      this.pedidoService.actualizarPedido(pedido);
    } else {
      this.pedidoService.guardarPedido(pedido);
    }

    this.mostrarPedidos();
    this.limpiar();
  }

  mostrarPedidos() {
    this.listaPedidos = this.pedidoService.mostrarPedidos();
  }

  editar(p: Pedido) {
    this.modoEdicion = true;
    this.idEditando = p.id;

    this.modeloPedido.set({
      clienteId: String(p.clienteId),
      estado: p.estado
    });

    this.carrito = [...p.detalles];
  }

  eliminar(id: number) {
    this.pedidoService.eliminarPedido(id);
    this.mostrarPedidos();
  }

  limpiar() {
    this.modeloPedido.set({
      clienteId: '',
      estado: 'PENDIENTE'
    });

    this.carrito = [];
  }

  // 📊 RESUMEN
  get pedidosPendientes() {
    return this.listaPedidos.filter(p => p.estado === 'PENDIENTE').length;
  }

  get pedidosEntregados() {
    return this.listaPedidos.filter(p => p.estado === 'ENTREGADO').length;
  }

  get totalVentas() {
    return this.listaPedidos.reduce((t, p) => t + p.total, 0);
  }

  getNombreCliente(id: number): string {
  const cliente = this.listaClientes.find(c => c.id === id);
  return cliente ? cliente.nombres : 'Desconocido';
}

getNombreVendedor(): string {
  const user = this.authService.getUsuarioActual();
  return user ? user.nombre : 'Sistema';
}
}
import { Component, inject, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Navbar } from '../../../layout/navbar/navbar';
import { Sidebar } from '../../../layout/sidebar/sidebar';
import { AuthService } from '../../../services/auth.service';
import { ProductoService } from '../../../services/producto.service';
import { ClienteService } from '../../../services/cliente.service';
import { PedidoService } from '../../../services/pedido.service';
import { ProveedorService } from '../../../services/proveedor.service';
import Chart from 'chart.js/auto';

@Component({
  selector: 'app-dashboard-home',
  standalone: true,
  imports: [Navbar, Sidebar, CommonModule],
  templateUrl: './dashboard-home.html',
  styleUrls: ['./dashboard-home.css']
})
export class DashboardHome {
  authService = inject(AuthService);
  productoService = inject(ProductoService);
  clienteService = inject(ClienteService);
  pedidoService = inject(PedidoService);
  proveedorService = inject(ProveedorService);

  rol = signal('');

  totalProductos = signal(0);
  totalClientes = signal(0);
  totalProveedores = signal(0);
  totalPedidos = signal(0);
  totalVentas = signal(0);
  stockBajo = signal(0);
  pedidosPendientes = signal(0);
  pedidosEntregados = signal(0);

  productos = signal<any[]>([]);
  pedidos = signal<any[]>([]);

  constructor() {
    this.rol.set(this.authService.getRol() || '');
    this.cargarDatos();
  }

  async cargarDatos() {
    const [productos, pedidos] = await Promise.all([
      this.productoService.listar(),
      this.pedidoService.listar()
    ]);

    this.productos.set(productos);
    this.pedidos.set(pedidos);
    this.totalProductos.set(productos.length);
    this.totalPedidos.set(pedidos.length);
    this.pedidosPendientes.set(pedidos.filter(p => p.estadoId === 1).length);
    this.pedidosEntregados.set(pedidos.filter(p => p.estadoId === 2).length);
    this.totalVentas.set(pedidos.reduce((t, p) => t + p.total, 0));
    this.stockBajo.set(productos.filter(p => p.stock <= 5).length);

    if (this.rol() === 'ADMIN' || this.rol() === 'VENDEDOR') {
      const clientes = await this.clienteService.listar();
      this.totalClientes.set(clientes.length);
    }

    if (this.rol() === 'ADMIN') {
      const proveedores = await this.proveedorService.listar();
      this.totalProveedores.set(proveedores.length);
    }

    setTimeout(() => this.recrearGraficos());
  }

  private recrearGraficos() {
    this.graficoPedidos();
    this.graficoStock();
    this.graficoVentas();
  }

  graficoPedidos() {
    if (!document.getElementById('chartPedidos')) return;
    const existing = Chart.getChart('chartPedidos');
    if (existing) existing.destroy();
    new Chart('chartPedidos', {
      type: 'pie',
      data: {
        labels: ['Pendientes', 'Entregados'],
        datasets: [{
          data: [this.pedidosPendientes(), this.pedidosEntregados()],
          backgroundColor: ['orange', 'green']
        }]
      }
    });
  }

  graficoStock() {
    if (!document.getElementById('chartStock')) return;
    const existing = Chart.getChart('chartStock');
    if (existing) existing.destroy();
    new Chart('chartStock', {
      type: 'bar',
      data: {
        labels: this.productos().map(p => p.nombre),
        datasets: [{
          label: 'Stock',
          data: this.productos().map(p => p.stock),
          backgroundColor: 'blue'
        }]
      }
    });
  }

  graficoVentas() {
    if (!document.getElementById('chartVentas')) return;
    const existing = Chart.getChart('chartVentas');
    if (existing) existing.destroy();
    new Chart('chartVentas', {
      type: 'doughnut',
      data: {
        labels: this.pedidos().map(p => 'Pedido ' + p.id),
        datasets: [{
          data: this.pedidos().map(p => p.total),
          backgroundColor: ['red', 'blue', 'green', 'orange', 'purple']
        }]
      }
    });
  }
}

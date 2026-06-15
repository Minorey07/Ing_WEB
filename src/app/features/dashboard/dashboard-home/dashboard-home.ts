import { Component, inject, AfterViewInit } from '@angular/core';

import { Navbar } from '../../../layout/navbar/navbar';
import { Sidebar } from '../../../layout/sidebar/sidebar';

import { ProductoService } from '../../../services/producto.service';
import { ClienteService } from '../../../services/cliente.service';
import { PedidoService } from '../../../services/pedido.service';

import Chart from 'chart.js/auto';

@Component({
  selector: 'app-dashboard-home',
  standalone: true,
  imports: [Navbar, Sidebar],
  templateUrl: './dashboard-home.html',
  styleUrls: ['./dashboard-home.css']
})
export class DashboardHome implements AfterViewInit {

  productoService = inject(ProductoService);
  clienteService = inject(ClienteService);
  pedidoService = inject(PedidoService);

  // ======================
  // DATA REAL
  // ======================
  get productos() {
    return this.productoService.mostrarProductos();
  }

  get clientes() {
    return this.clienteService.mostrarClientes();
  }

  get pedidos() {
    return this.pedidoService.mostrarPedidos();
  }

  get pedidosPendientes() {
    return this.pedidos.filter(p => p.estado === 'PENDIENTE').length;
  }

  get pedidosEntregados() {
    return this.pedidos.filter(p => p.estado === 'ENTREGADO').length;
  }

  get totalVentas() {
    return this.pedidos.reduce((t, p) => t + p.total, 0);
  }

  // ======================
  // CHARTS
  // ======================
  ngAfterViewInit() {
    this.graficoPedidos();
    this.graficoStock();
    this.graficoVentas();
  }

  graficoPedidos() {
    new Chart('chartPedidos', {
      type: 'pie',
      data: {
        labels: ['Pendientes', 'Entregados'],
        datasets: [{
          data: [
            this.pedidosPendientes,
            this.pedidosEntregados
          ],
          backgroundColor: ['orange', 'green']
        }]
      }
    });
  }

  graficoStock() {
    new Chart('chartStock', {
      type: 'bar',
      data: {
        labels: this.productos.map(p => p.nombre),
        datasets: [{
          label: 'Stock',
          data: this.productos.map(p => p.stock),
          backgroundColor: 'blue'
        }]
      }
    });
  }

  graficoVentas() {
    new Chart('chartVentas', {
      type: 'doughnut',
      data: {
        labels: this.pedidos.map(p => 'Pedido ' + p.id),
        datasets: [{
          data: this.pedidos.map(p => p.total),
          backgroundColor: ['red', 'blue', 'green', 'orange', 'purple']
        }]
      }
    });
  }
}
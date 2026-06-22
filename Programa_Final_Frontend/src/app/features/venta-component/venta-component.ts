import { Component, inject, signal } from '@angular/core';
import { PedidoService } from '../../services/pedido.service';
import { Pedido } from '../../models/pedido.model';

@Component({
  selector: 'app-venta-component',
  imports: [],
  templateUrl: './venta-component.html',
  styleUrl: './venta-component.css',
})
export class VentaComponent {
  pedidoService = inject(PedidoService);
  listaVentas = signal<Pedido[]>([]);
  expandido = signal<Set<number>>(new Set());

  constructor() {
    this.cargarVentas();
  }

  async cargarVentas() {
    const pedidos = await this.pedidoService.listar();
    this.listaVentas.set(pedidos.filter(p => p.estadoId === 2));
  }

  get totalVentas(): number {
    return this.listaVentas().reduce((t, v) => t + v.total, 0);
  }

  toggleExpand(id: number) {
    const s = new Set(this.expandido());
    if (s.has(id)) { s.delete(id); } else { s.add(id); }
    this.expandido.set(s);
  }
}
